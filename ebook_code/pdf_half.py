import fitz

inp=fitz.open("cheka_cropped.pdf")
out=fitz.open()

for i in range(0,len(inp),2):
    p1=inp.load_page(i)
    p2=inp.load_page(i+1) if i+1<len(inp) else None

    w=p1.rect.width
    h=p1.rect.height

    new=out.new_page(width=w,height=h*2)

    new.show_pdf_page(fitz.Rect(0,0,w,h),inp,i)
    if p2:
        new.show_pdf_page(fitz.Rect(0,h,w,2*h),inp,i+1)

out.save("cheka_cropped_2up.pdf")