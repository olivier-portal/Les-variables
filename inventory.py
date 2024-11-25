product_detail = {
    "article": "chemise",
    "price": 65,
    "quantity": 52,
}

print(f'Informations du produit ====> Nom : {product_detail.get("article")}, prix : {product_detail.get("price")}€, Quantité : {product_detail.get("quantity")}, "voulez-vous en achetez ?", "O/N"')

user_choice = input()

if user_choice == "O":
    print("Combien voulez-vous en acheter ?")
    number_order = int(input())
    if number_order <= product_detail["quantity"]:
        product_detail["quantity"] -= number_order
        print(f"Quantité restante : {product_detail["quantity"]}")
    else:
        print("Désolé nous n'avons pas assez de stock !")  
else:
    print("Dommage ! Peut-être une autre fois !")

