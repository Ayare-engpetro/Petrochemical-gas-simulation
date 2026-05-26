import math

def calculate_pressures():
    print("--- Simulation of Petrochemical Gas Pressures ---")
    try:
        # Input Parameters
        T = float(input("Enter Temperature T (in Kelvin, e.g., 300): "))
        V = float(input("Enter Molar Volume V (in L/mol, e.g., 2.5): "))
        
        # Gas constants
        R = 0.0821
        a = 5.489  
        b = 0.0638 
        
        if V <= b:
            print("\n[Error] Molar volume V must be greater than co-volume b.")
            return

        # Calculations
        P_ideal = (R * T) / V
        P_real = ((R * T) / (V - b)) - (a / (V ** 2))
        
        # Results
        print("\n================ RESULTS ================")
        print(f"Ideal Gas Pressure: {P_ideal:.4f} atm")
        print(f"Real Gas Pressure (Van der Waals): {P_real:.4f} atm")
        print(f"Pressure Difference: {abs(P_ideal - P_real):.4f} atm")
        print("=========================================")
    except ValueError:
        print("\n[Error] Please enter valid numerical values.")

if __name__ == "__main__":
    calculate_pressures()
