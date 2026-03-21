import codecs
import re

with codecs.open("public/index.html", "r", "utf-8") as f:
    text = f.read()

# I will find the end of Step 3 h3
match_step3 = re.search(r'<h3[^>]*>3\. הדרכה והעברת מקל</h3>', text)
if match_step3:
    valid_process_end = match_step3.end()
    print("Found Step 3 h3 at index", valid_process_end)

original_p = """
                        <p class="text-lg text-slate-500 leading-relaxed flex-grow">
                            בסיום ההטמעה, הצוות שלכם מקבל הדרכה מקיפה וליווי צמוד כדי שינהלו את המערכת בעצמאות מלאה.
                        </p>
"""

# Extract the Lead Magnet
match_lead_magnet = re.search(r'<!-- ── Section 3\.5: Lead Magnet ── -->.*?</section>', text, re.DOTALL)
if match_lead_magnet:
    lead_magnet_html = match_lead_magnet.group(0)
    print("Extracted Lead Magnet")

# Extract the FAQ questions list
match_faq = re.search(r'<div class="space-y-5">\s*<!-- Q1 -->.*?<!-- ── Section 5: Contact Form ── -->', text, re.DOTALL)
if match_faq:
    faq_questions_only = text[match_faq.start():match_faq.end() - len('<!-- ── Section 5: Contact Form ── -->')]
    print("Extracted FAQ questions")

# Reconstruct perfectly:
part1 = text[:valid_process_end]

closing_process = """
                    </div>
                </div>
            </div>
        </section>
"""

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

match_contact = re.search(r'<!-- ── Section 5: Contact Form ── -->', text)
if match_contact:
    part_rest = text[match_contact.start():]
    
final_text = part1 + original_p + closing_process + "\n        " + lead_magnet_html + "\n\n" + faq_header + faq_questions_only + faq_footer + "\n\n        " + part_rest

with codecs.open("public/index.html", "w", "utf-8") as f:
    f.write(final_text)

print("Repair perfectly completed.")
