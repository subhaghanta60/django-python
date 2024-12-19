from core.models import Restaurant,Rating,User,Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint


#def run():
    

    
    
    # restaurant = Restaurant()
    # restaurant.name = "My Italian Restaurant"
    # restaurant.data_opened = timezone.now()
    # restaurant.latitude = 50.2
    # restaurant.longitude = 54.5
    # restaurant.restaurant_type=Restaurant.TypeChoices.ITALIAN
    
    # restaurant.save()

    # restaurants = Restaurant.objects.all()
    # print(restaurants)
    # print(connection.queries)
    
    # restaurant= Restaurant.objects.first()
    # print(restaurant)
    # print(connection.queries)


    # Restaurant.objects.create(
    #     name= "Pizza shop",
    #     data_opened= timezone.now(),
    #     restaurant_type=Restaurant.TypeChoices.ITALIAN,
    #     latitude=50.2,
    #     longitude=50.5
    # )
    
    # # Print the SQL queries executed
    # for query in connection.queries:
    #     print(query['sql'])
    # print(Restaurant.objects.count())
    #  print(Restaurant.objects.last())
    # print(connection.queries)

    # restaurant = Restaurant.objects.last()
    # user = User.objects.first()

    # Rating.objects.create(user=user,restaurant=restaurant, rating=3.2)
    # print(Rating.objects.all())
    # print(Rating.objects.filter(rating=3))
    # print(Rating.objects.filter(rating=10))
    # print(Rating.objects.filter(rating__gte=3))
    # print(Rating.objects.exclude(rating__lte=3))
    # restaurant = Restaurant.objects.first()
    # print(restaurant.name)

    # restaurant.name = "My Father Italian Reasurent"
    # restaurant.save()

    # pprint(connection.queries)

    # rating = Rating.objects.first()
    # print(rating.restaurant)

    # restaurant= Restaurant.objects.first()
    # print(restaurant.ratings.all())
    # pprint(connection.queries)


    # Sale.objects.create(
    #     restaurant = Restaurant.objects.last(),
    #     income=9.33,
    #     datetime=timezone.now()
    # )
    # Sale.objects.create(
    #     restaurant = Restaurant.objects.last(),
    #     income=1.25,
    #     datetime=timezone.now()
    # )
    # Sale.objects.create(
    #     restaurant = Restaurant.objects.last(),
    #     income=4.45,
    #     datetime=timezone.now()
    # )
    #  restaurant=Restaurant.objects.first()
    #  print(restaurant.sales.all())

    # user =User.objects.first()
    # restaurant = Restaurant.objects.first()

    # rating,created = Rating.objects.get_or_create(
    #     restaurant=restaurant,
    #     user=user,
    #     rating=7
    # )

    # if created:
    #     print("Welcome To Our Team")

    # pprint(connection.queries)

def run():
    user=User.objects.first()
    restaurant= Restaurant.objects.first()

    rating = Rating(user=user,restaurant=restaurant,rating=10)

    rating.full_clean()
    rating.save()
    
   