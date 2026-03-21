import codecs
import re

with codecs.open("public/index.html", "r", "utf-8") as f:
    text = f.read()

# I will find the end of Step 3 manually
# "3. הדרכה והעברת מקל" is at index X
match_step3 = re.search(r'<h3[^>]*>3\. הדרכה והעברת מקל</h3>', text)
if match_step3:
    pos = match_step3.end()
    # The paragraph right after it is:
    # <p class="text-lg text-slate-500 leading-relaxed flex-grow">
    #     בסיום ההטמעה...
    # </p>
    # Find the closing </p> after the h3
    match_p = re.search(r'</p>', text[pos:])
    if match_p:
        valid_process_end = pos + match_p.end()
        print("Found valid end of Step 3 text at index", valid_process_end)
        
# Now we need to extract the Lead Magnet out of the garbage
match_lead_magnet = re.search(r'<!-- ── Section 3\.5: Lead Magnet ── -->.*?</section>', text, re.DOTALL)
if match_lead_magnet:
    lead_magnet_html = match_lead_magnet.group(0)
    print("Extracted Lead Magnet")

# And we need to extract the raw FAQ questions list
# It starts with `<div class="space-y-5">` and ends right before `<!-- ── Section 5: Contact Form ── -->`
match_faq = re.search(r'<div class="space-y-5">\s*<!-- Q1 -->.*?<!-- ── Section 5: Contact Form ── -->', text, re.DOTALL)
if match_faq:
    # We grab just the space-y-5 div and its details
    faq_questions_only = text[match_faq.start():match_faq.end() - len('<!-- ── Section 5: Contact Form ── -->')]
    print("Extracted FAQ questions")

# We reconstruct perfectly:
# 1. Everything up to the valid_process_end
part1 = text[:valid_process_end]
# Add the missing closing tags for the Process section
closing_process = """
                    </div>
                </div>
            </div>
        </section>
"""

# 2. Add the Lead Magnet
# 3. Add the FAQ section WITH ITS PROPER HEADER
faq_header = """
        <!-- ── Section 4: FAQ ── -->
        <section class="py-24 px-6 bg-alt relative overflow-hidden" reveal-element>
            <div class="container mx-auto max-w-3xl relative z-10">
                <div class="text-center mb-16">
                    <h2 class="text-4xl md:text-5xl font-bold text-primary tracking-tight">שאלות נפוצות</h2>
                </div>
"""
faq_footer = """
            </div>
        </section>
"""

# 4. Add Contact Form and the rest of the file
match_contact = re.search(r'<!-- ── Section 5: Contact Form ── -->', text)
if match_contact:
    part_rest = text[match_contact.start():]
    
final_text = part1 + closing_process + "\n" + lead_magnet_html + "\n\n" + faq_header + faq_questions_only + faq_footer + "\n" + part_rest

with codecs.open("public/index.html", "w", "utf-8") as f:
    f.write(final_text)

print("Repair completed seamlessly.")
