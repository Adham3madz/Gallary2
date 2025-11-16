from flask import Flask, render_template

app = Flask(__name__)

# --- UPDATED DATA STRUCTURE: CORRECTED IMAGE FILENAMES ---
gallery_items = [
    {
        "id": 1,
        # Updated description for accuracy based on the image content (a collection of antiques)
        "description": "Antique Clocks and Vases Collection", 
        "price": "EGP 3,500.00",
        "category": "antiques",
        # FIX: Changed file extension from .png to .jpg
        "images": ["image copy 3.jpg"] 
    },
    {
        "id": 2,
        "description": "Old Pharaonic Coin",
        "price": "EGP 1,200.00",
        "category": "coins",
         # Correct: coin-obverse.jpg was uploaded
        "images": ["coin-obverse.jpg"]
    },
    {
        "id": 3,
        "description": "Vintage Wooden Chair Set",
        "price": "EGP 5,000.00",
        "category": "furniture",
        # Correct: chair-front.jpg and chair-detail.jpg were uploaded
        "images": ["chair-front.jpg", "chair-detail.jpg"] 
    },
    {
        "id": 4,
        "description": "Ancient Gold Coin",
        "price": "EGP 2,100.00",
        "category": "coins",
        # Correct: item1.jpg and item2.jpg were uploaded
        "images": ["item1.jpg", "item2.jpg"] 
    }
]

# This list is for the filter buttons, it doesn't change
category_list = ["all", "coins", "antiques", "furniture"]


@app.route('/')
def home():
    # This logic doesn't need to change at all!
    # We just pass the new gallery_items structure.
    return render_template('index.html', 
                           items=gallery_items, 
                           categories=category_list)

if __name__ == '__main__':
    app.run(debug=True)