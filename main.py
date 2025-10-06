from js import document

# Basic Info
resto_name = "Ethanol's Burger"
owner_name = "Ethanol"
year_established = 2025
business_hours = "7:30 AM - 3:30 PM"
has_delivery = True

# Menu
menu_prices = {
    "Big Boy": 120.20,
    "OG Burger": 95.50,
    "Sheer Heart Attack": 150.75,
    "Double Trouble": 135.00,
    "Cheesy Melt": 110.00
}

# Fill Header
document.getElementById("restoName").innerText = resto_name
document.getElementById("ownerName").innerText = f"Owner: {owner_name}"
document.getElementById("yearEstablished").innerText = f"Since {year_established}"
document.getElementById("business_hours").innerText = business_hours
document.getElementById("delivery_btn").innerText = "🚚 Delivery Available" if has_delivery else "❌ No Delivery"

# Fill Menu Table
menu_table = document.getElementById("menu_items")
for product, price in menu_prices.items():
    row_html = f"<tr><td>{product}</td><td>₱{price:.2f}</td></tr>"
    menu_table.innerHTML += row_html
