import pandas as pd
import random
from random import randint
from faker import Faker


fake = Faker()

# Define the number of users, products and interactions
num_users = 100
num_products = 50
num_interactions = 1000

# Generate users and products
users = [fake.uuid4() for _ in range(num_users)]
products = [fake.uuid4() for _ in range(num_products)]

# Define the types of interactions
interaction_types = ['view', 'click', 'purchase']

# Generate interactions
interactions = []
for _ in range(num_interactions):
    user = random.choice(users)
    product = random.choice(products)
    interaction_type = random.choice(interaction_types)
    timestamp = fake.date_time_this_year()

    interactions.append([user, product, interaction_type, timestamp])

# Create a DataFrame
df = pd.DataFrame(interactions, columns=['user_id', 'product_id', 'interaction_type', 'timestamp'])

# Save to CSV
df.to_csv('user_interactions.csv', index=False)


