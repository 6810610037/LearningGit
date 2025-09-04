# โกมล บุญเรือง
energy_unit = int(input("Enter the energy consumption (kilowatt-hours): "))
SERVICE_CHARGE = 24.62
UNIT_RATE = 0
if energy_unit >= 1 :
    if energy_unit >150:
        BASE_UNIT = 150
        energy_between_1to_149 = energy_unit-BASE_UNIT 
        UNIT_RATE = 3.2484
        electric_cost = energy_between_1to_149 * UNIT_RATE
    else:
        UNIT_RATE = 3.2484
        electric_cost = energy_unit * UNIT_RATE
if energy_unit > 150 :
    energy_above_150 = energy_unit - 150
    UNIT_RATE = 4.2218
    cost_above_150 = energy_above_150 * UNIT_RATE
    electric_cost += cost_above_150
if energy_unit > 400:
    energy_above_400 = energy_unit - 400
    UNIT_RATE = 4.4217
    cost_above_400 = energy_above_400 * UNIT_RATE
    electric_cost += cost_above_400
if energy_unit == 0:
    electric_cost = energy_unit * UNIT_RATE
VAT = (electric_cost + SERVICE_CHARGE) * 7 / 100
total_cost = electric_cost + SERVICE_CHARGE + VAT
print(f"Electricity cost = {electric_cost:,.2f} Baht")
print(f"Service charge = {SERVICE_CHARGE} Baht")
print(f"VAT (7 percent) = {VAT:,.2f} Baht")
print(f"Total cost = {total_cost:,.2f} Baht")
