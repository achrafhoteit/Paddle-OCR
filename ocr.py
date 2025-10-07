# from paddleocr import PaddleOCR

# ocr = PaddleOCR(
#     lang="ar",                       # Arabic
#     use_angle_cls=False,
#     use_doc_orientation_classify=False,
#     use_doc_unwarping=False,
#     use_textline_orientation=False,
# )

# # Local file path works too (not just a URL)
# result = ocr.predict(input="02_text.png")

# # Quick look + artifacts
# for r in result:
#     r.print()                 # pretty console print
#     r.save_to_img("output")   # writes annotated image(s)
#     r.save_to_json("output")  # writes structured JSON

from paddleocr import PaddleOCR

ocr = PaddleOCR(
    lang="ar",
    use_textline_orientation=False,   # keep only this (new flag)
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
)

result = ocr.predict(input="02_text.png")
for r in result:
    r.print()               # quick console view
    r.save_to_img("output")
    r.save_to_json("output")  # parse JSON for plain text if needed