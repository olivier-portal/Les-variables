# Define article
product_detail = {
    "article": "chemise",
    "price": 65,
    "quantity": 52,
}

# Show details of the article and ask if user want to buy some - modify quantity if user buy
print(f'Informations du produit ====> Nom : {product_detail.get("article")}, prix : {product_detail.get("price")}€, Quantité : {product_detail.get("quantity")}, "voulez-vous en achetez ?", "O/N"')

user_choice = input()

if user_choice == "O" or user_choice == "o":
    print("Combien voulez-vous en acheter ?")
    number_order = int(input())
    if number_order <= product_detail["quantity"]:
        product_detail["quantity"] -= number_order
        print(f"Quantité restante : {product_detail["quantity"]}")
    else:
        print("Désolé nous n'avons pas assez de stock !")  
elif user_choice == "N" or user_choice == "n":
    print("Dommage ! Peut-être une autre fois !")
else:
    print("Il faut répondre O pour oui ou N pour non")
    
# Increase price by 10%
product_detail["price"] = 65 * 1.1
product_detail
print(f'Informations du produit ====> Nom : {product_detail.get("article")}, prix : {product_detail.get("price")}€, Quantité : {product_detail.get("quantity")}')
