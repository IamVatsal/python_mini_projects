import json
import requests

API_KEY = "YOUR_API_KEY"  # Replace with your actual API key if needed
# This API key is just a placeholder; you need to get your own from the exchange rate API service.


def get_exchange_rates(crr: str) -> dict:
    """
    Get exchange rates for a specific base currency.
    
    Args:
        crr (str): The base currency code (e.g., 'USD').
    
    Returns:
        dict: The exchange rates data.
    """
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{crr}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch exchange rates")


def save_rates_to_file(rates: dict, filename: str = 'rate.json') -> None:
    """
    Save exchange rates to a JSON file.
    
    Args:
        rates (dict): The exchange rates data.
        filename (str): The filename to save to.
    """
    with open(filename, 'w') as file:
        json.dump(rates, file, indent=4)


def load_rates_from_file(filename: str = 'rate.json') -> dict:
    """
    Load exchange rates from a JSON file.
    
    Args:
        filename (str): The filename to load from.
    
    Returns:
        dict: The exchange rates data.
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def convert_money(rates: dict, base: str, to: str, money: float) -> float:
    """
    Convert money from one currency to another.
    
    Args:
        rates (dict): The exchange rates data.
        base (str): The base currency code.
        to (str): The target currency code.
        money (float): The amount to convert.
    
    Returns:
        float: The converted amount, or None if conversion fails.
    """
    if not rates:
        print("No exchange rates available.")
        return None
    
    conversion_rates = rates.get('conversion_rates', {})
    
    if not conversion_rates:
        print("No conversion rates found in data.")
        return None
    
    # Check if both currencies exist in the rates
    if base not in conversion_rates or to not in conversion_rates:
        print(f"Currency {base} or {to} not found in exchange rates.")
        return None
    
    # Convert from base currency to target currency
    # If base is USD (rate = 1), multiply by target rate
    # If base is not USD, first convert to USD, then to target
    base_rate = conversion_rates.get(base)
    to_rate = conversion_rates.get(to)
    
    # Convert to USD first, then to target currency
    usd_amount = money / base_rate
    converted_money = usd_amount * to_rate
    
    return converted_money


def main():
    """
    Main function to run the currency converter.
    """
    print("Welcome to Currency Converter")
    print("=" * 40)
    
    # Load rates from file
    rates = load_rates_from_file()
    
    # If no rates available, try to fetch from API
    if not rates:
        print("No rates found in file. Fetching from API...")
        try:
            base_currency = "USD"  # Default base currency
            rates = get_exchange_rates(base_currency)
            save_rates_to_file(rates)
            print("Rates fetched and saved successfully.")
        except Exception as e:
            print(f"Failed to fetch rates: {e}")
            return
    
    # Get user input
    try:
        base = input("Enter Base Currency (e.g., USD): ").upper()
        to = input("Enter Target Currency (e.g., EUR): ").upper()
        
        # Convert input to float instead of using ToInt
        while True:
            try:
                money = float(input("Enter Money To Convert: "))
                break
            except ValueError:
                print("Please enter a valid number.")
        
        # Convert money
        converted = convert_money(rates, base, to, money)
        
        if converted is not None:
            print(f"\n{money} {base} = {converted:.2f} {to}")
        else:
            print("Conversion failed.")
            
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()