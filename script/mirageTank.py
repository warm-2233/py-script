from PIL import Image
import sys



def gen_tank(a,b):
    img = Image.new("RGBA", (a.width, a.height))
    
    for w in range(img.width):
        for h in range(img.height):
            pixel_a = a.getpixel((w,h))
            
            pixel_b = b.getpixel((w,h))
            
            
            alpha = 255 - (pixel_a - pixel_b)
            # print("a",pixel_a, "----b", pixel_b)
            
            if pixel_a == 0 or pixel_b == 0:
                gray = 0
            else:
                gray = int(255 * pixel_a / pixel_b)
            
            
            img.putpixel( (w,h), (gray, gray, gray, alpha) )
        
    return img
    

if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        a = input("a img:")
        b = input("b img:")
        out = input("out img name :")
    elif len(sys.argv) != 4:
        print("python", sys.argv[0], "a-img b-img out-img")
        sys.exit()
    else:
        a = sys.argv[1]
        b = sys.argv[2]
        out = sys.argv[3]
    
    a = Image.open(a).convert("L")
    b = Image.open(b).convert("L")
    
    img = gen_tank(a,b)
    
    img.save(out)
    
    
    
    
    
    
    
    
    
    
    
    
    