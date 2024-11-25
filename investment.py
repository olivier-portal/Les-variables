# gain annuel suivant le rendement pour un montant initial
initial_amount = 10000
annual_rate = 1.04

annual_gain = initial_amount * annual_rate - initial_amount

print(f"Votre gain annuel à été de :  {annual_gain}")

# Le rendement augmente de 2% et le montant initial de 5000€

new_amount = initial_amount + annual_gain + 5000
new_rate = annual_rate + 0.02

new_annual_gain = new_amount * new_rate - new_amount

print(f"Votre gain annuel à été de :  {new_annual_gain}")

# Un retrait de 10% est effectué, le taux baisse d'1%

amount_year3 = (new_amount + new_annual_gain) - ((new_amount + new_annual_gain) * 0.1)
print(amount_year3)
rate_year3 = new_rate - 0.01

annual_gain_year3 = amount_year3 * rate_year3 - amount_year3

total_gain = amount_year3 + annual_gain_year3

print(f"Votre solde est de : {total_gain} Votre gain annuel à été de :  {annual_gain_year3}")