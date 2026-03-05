class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, letter):
        result = []
        for product in self.products:
            if product.startswith(letter):
                result.append(product)
        return result

    def __repr__(self):
        sorted_products = sorted(self.products)
        items = " ".join(sorted_products)
        return f"Items in the {self.name} catalogue: {items}"
            
    
