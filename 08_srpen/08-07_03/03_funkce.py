
def test_heslo(heslo: str) -> bool:
  return len(heslo) >= 5

# Příklad použití:
print(test_heslo('1234'))  # Vrátí False
print(test_heslo('12345'))  # Vrátí True
print(test_heslo('TajnéHeslo'))  # Vrátí True