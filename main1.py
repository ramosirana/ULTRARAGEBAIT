from pyscript import display
from js import document

# Titles
snzn = "Mikainan! Order Form"
lol = "Menu"
display(snzn, target="sns")
display(lol, target="Menu")

# Function to show order summary and reset form
def show_order_summary(event):
    form = document.getElementById("order-form")
    name = document.getElementById("cust-name").value
    address = document.getElementById("cust-address").value
    contact = document.getElementById("cust-contact").value

    # Check selected menu items and calculate total
    total = 0
    items = []
    for i in range(1, 6):
        checkbox = document.getElementById(f"op{i}")
        if checkbox.checked:
            items.append(checkbox.nextElementSibling.innerText)
            total += int(checkbox.value)

    # Build order text
    order_text = f"""
    Order for: {name}  
    Address: {address}  
    Contact number: {contact}  
    Items Ordered: {", ".join(items) if items else "None"}  
    Total: ₱ {total}.00
    """

    # Display in summary div
    order_div = document.getElementById("order-summary")
    order_div.style.display = "block"
    order_div.innerHTML = ""  # clear old content
    display(order_text, target="order-summary")

    # Reset form after submission
    form.reset()

# Attach button event
document.getElementById("generate-btn").addEventListener("click", show_order_summary)
