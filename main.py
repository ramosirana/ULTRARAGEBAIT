from js import document

# resto info
restname = "Mikainan!"
owname = "miggy"
yestablished = 2025
bours = "6:07 AM - 6:07 PM"
has_delivery = True

# menu
menu_prices = {
    "The Miggy Tapsi": 130.00,
    "The Miggy Toci": 130.00,
    "The Miggy Hotsi": 120.00,
    "The Miggy Spamsi": 120.00,
    "The Miggy Bangsi": 120.00
}

# header
document.getElementById("restoName").innerText = restname
document.getElementById("ownerName").innerText = f"Owner: {owname}"
document.getElementById("yearEstablished").innerText = f"Since {yestablished}"
document.getElementById("business_hours").innerText = bours
document.getElementById("delivery_btn").innerText = "We can deliver!" if has_delivery else "We can't deliver!"

# menu table
menu_table = document.getElementById("menu_items")
for product, price in menu_prices.items():
    row_html = f"<tr><td>{product}</td><td>₱{price:.2f}</td></tr>"
    menu_table.innerHTML += row_html
