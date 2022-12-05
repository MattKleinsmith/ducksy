## API documentation

- [Sessions](#sessions)
- [Users](#users)
- [Products](#products)
- [Reviews](#reviews)
- [Product images](#product-images)
- [Review images](#review-images)

## User sessions

<details>
<summary style="font-size: 18px; font-weight: 500">CREATE: Log in a user: <code>POST /api/session</code></summary><br>

Request:

```javascript
Content-Type: "application/json",
Body:
{
    "email": "john.smith@gmail.com"
    "password": "secret password"
}
```

  ---

Response:

```javascript
Status: 200,
Content-Type: "application/json",
Body:
{
  "id": 1,
  "first_name": "John",
  "email": "john.smith@gmail.com",
  "profile_picture_url": "john.png"
}
```

<details>
<summary>Errors</summary><br>
Invalid Credentials

```javascript
Status: 401,
Content-Type: "application/json",
Body:
{
  "message": "Invalid credentials",
  "statusCode": 401
}
```

Body validation errors

```javascript
Status: 400,
Content-type: "application/json",
Body:
{
  "message": "Validation error",
  "statusCode": 400,
  "errors": {
    "credential": "Email is required",
    "password": "Password is required"
  }
}
```
</details>

</details>


<details>
<summary style="font-size: 18px; font-weight: 500">READ: Get the current user: <code>GET /api/session</code></summary><br>

Response:

```javascript
Status: 200,
Content-Type: "application/json",
Body:
{
  "id": 1,
  "first_name": "John",
  "email": "john.smith@gmail.com",
  "profile_picture_url": "john.png"
}
```

</details>

<details>
<summary style="font-size: 18px; font-weight: 500">DELETE: Log out the current user: <code>DELETE /api/session</code></summary><br>

Response:

```javascript
Status: 200,
Content-Type: "application/json",
Body:
{
  "message": "Successfully deleted",
  "statusCode": 200
}
```

</details>

<br>

## Users


<details>
<summary style="font-size: 18px; font-weight: 500">CREATE: Sign up a user: <code>POST /api/users</code></summary><br>

Request:

```javascript
Content-Type: "application/json",
Body:
{
  "first_name": "John",
  "email": "john.smith@gmail.com",
  "password": "secret password"
}
```

  ---

Response:

```javascript
Status: 201,
Content-Type: "application/json",
Body:
{
  "id": 1,
  "first_name": "John",
  "email": "john.smith@gmail.com",
  "profile_picture_url": "john.png"
}
```

  <details>
<summary>Errors</summary><br>
User already exists with the specified email

```javascript
Status: 403,
Content-Type: "application/json",
Body:
{
  "message": "User already exists",
  "statusCode": 403,
  "errors": {
    "email": "User with that email already exists"
  }
}
```

Body validation errors

```javascript
Status: 400,
Content-Type: "application/json",
Body:
{
  "message": "Validation error",
  "statusCode": 400,
  "errors": {
    "email": "Invalid email",
    "first_name": "First name is required",
  }
}
```
</details>

</details>

<details>
<summary style="font-size: 18px; font-weight: 500">UPDATE: Update a user: <code>PATCH /api/users/:user_id</code></summary><br>

The user must be logged in to update their account.

Request:

```javascript
Content-Type: "application/json",
Body:
{
  "profile_picture_url": "new_john.png"
}
```

  ---

Response:

```javascript
Status: 200,
Content-Type: "application/json",
Body:
{
  "id": 1,
  "first_name": "John",
  "email": "john.smith@gmail.com",
  "profile_picture_url": "new_john.png"
}
```

</details>

<details>
<summary style="font-size: 18px; font-weight: 500">DELETE: Delete a user: <code>DELETE /api/users/:user_id</code></summary><br>

The user must be logged in to delete their account.

Response

```javascript
Status: 200,
Content-Type: "application/json",
Body:
{
  "message": "Successfully deleted",
  "statusCode": 200
}
```

</details>

<br>

## Products

<details>
<summary style="font-size: 18px; font-weight: 500">CREATE: Create a product: <code>POST /api/products</code></summary><br>

Request

```javascript
Content-Type: "application/json",
Body:
{
  "user_id": 1,
  "name": "Lamb Plush"
  "price": 20.00,
  "description": "Hand woven lamb plush."
}
```

---

Response

```javascript
Status: 201,
Content-Type: "application/json",
Body:
{
  "id": 1,
  "ownerId": 1,
  "user_id": 1,
  "name": "Lamb Plush"
  "price": 20.00,
  "description": "Hand woven lamb plush."
}
```

<details>
<summary>Errors</summary><br>

Body validation error

```javascript
Status: 400,
Content-Type: "application/json",
Body:
{
  "message": "Validation Error",
  "statusCode": 400,
  "errors": {
    "name": "Product name is required",
    "price": "Price is required",
    "description": "Description is required",
  }
}
```

  </details>

</details>

<details>
    <summary style="font-size: 18px; font-weight: 500">READ: Get products: <code>GET /api/products</code></summary><br>

    Response

    ```javascript
    Status: 200,
    Content-Type: "application/json",
    Body:
    {
    "Products": [
        {
        "id": 1,
        "user_id": 1,
        "name": "Woven Holiday Tree"
        "price": 112.57,
        "description": "Hand woven with a variety of shades of green to create a one of a kind holiday tree."
        "rating": 5.0,
        "preview_image": "tree.png"
        },
        {
        "id": 1,
        "user_id": 2,
        "name": "Carrot Plush"
        "price": 7.00,
        "description": "Hand woven carrot plush."
        "rating": 5.0,
        "preview_image": "carrot_plush.png"
        }
    ]
    }
    ```

</details>

<details>
<summary style="font-size: 18px; font-weight: 500">READ: Get products owned by the current user: <code>GET /api/products/current</code></summary><br>

Response

```javascript
Status: 200,
Content-Type: "application/json",
Body:
{
  "Products": [
    {
      "id": 1,
      "user_id": 1,
      "name": "Woven Holiday Tree"
      "price": 112.57,
      "description": "Hand woven with a variety of shades of green to create a one of a kind holiday tree."
      "rating": 5.0,
      "preview_image": "tree.png"
    }
  ]
}
```

</details>

<details>
<summary style="font-size: 18px; font-weight: 500">UPDATE: Update a product: <code>PATCH /api/products/:product_id</code></summary><br>

The user must be logged in to update their account.

Request:

```javascript
Content-Type: "application/json",
Body:
{
  "profile_picture_url": "new_john.png"
}
```

  ---

Response:

```javascript
Status: 200,
Content-Type: "application/json",
Body:
{
  "id": 1,
  "first_name": "John",
  "email": "john.smith@gmail.com",
  "profile_picture_url": "new_john.png"
}
```

</details>

<details>
<summary style="font-size: 18px; font-weight: 500">DELETE: Delete a product's image: <code>DELETE /api/products/:product_id</code></summary><br>

Response

```javascript
Status: 200,
Content-Type: "application/json",
Body:
{
  "message": "Successfully deleted",
  "statusCode": 200
}
```

</details>

<br>

## Reviews

<details>
<summary style="font-size: 18px; font-weight: 500">CREATE: Create a review: <code>POST /api/products/:product_id/reviews</code></summary><br>

Request

```javascript
Content-Type: "application/json",
Body:
{
  "user_id": 1,
  "product_id": 1,
  "rating": 5.0
  "review": "It is cute."
}
```

---

Response

```javascript
Status: 201,
Content-Type: "application/json",
Body:
{
  "id": 3,
  "user_id": 1,
  "product_id": 1,
  "rating": 5.0
  "review": "It is cute."
}
```

<details>
<summary>Errors</summary><br>
Body validation error

```javascript
Status: 400,
Content-Type: "application/json",
Body:
{
  "message": "Validation Error",
  "statusCode": 400,
  "errors": {
    "rating": "Rating is required",
    "review": "Review is required",
  }
}
```

</details>
</details>

<details>
<summary style="font-size: 18px; font-weight: 500">READ: Get reviews of a product: <code>GET /api/products/:product_id/reviews</code></summary><br>

Response

```javascript
Status: 200,
Content-Type: "application/json",
Body:
{
  "Reviews": [
    {
      "id": 1,
      "user_id": 1,
      "product_id": 1,
      "rating": 5.0
      "review": "It is soft."
    },
    {
      "id": 2,
      "user_id": 2,
      "product_id": 1,
      "rating": 5.0
      "review": "It is colorful."
    },
  ]
}
```

</details>

<details>
<summary style="font-size: 18px; font-weight: 500">DELETE: Delete a review: <code>DELETE /api/reviews/:review_id</code></summary><br>

Response

```javascript
Status: 200,
Content-Type: "application/json",
Body:
{
  "message": "Successfully deleted",
  "statusCode": 200
}
```

</details>

<br>

## Product images

<details>
<summary style="font-size: 18px; font-weight: 500">CREATE: Create an image for a product: <code>POST /api/products/:product_id/images</code></summary><br>

Request

```javascript
Content-Type: "application/json",
Body:
{
    "product_id": 1,
    "url": "tree3.png",
    "preview": false
}
```

---

Response

```javascript
Status: 201,
Content-Type: "application/json",
Body:
{
  "id": 3,
  "product_id": 1,
  "url": "tree3.png",
  "preview": false
}
```

</details>

<details>
<summary style="font-size: 18px; font-weight: 500">READ: Get images of a product: <code>GET /api/products/:product_id/images</code></summary><br>

Response

```javascript
Status: 200,
Content-Type: "application/json",
Body:
{
  "Images": [
    {
      "id": 1,
      "product_id": 1,
      "url": "tree.png",
      "preview": true
    },
    {
      "id": 2,
      "product_id": 1,
      "url": "tree2.png",
      "preview": false
    },
  ]
}
```

</details>

<details>
<summary style="font-size: 18px; font-weight: 500">DELETE: Delete a product's image: <code>DELETE /api/product_images/:product_image_id</code></summary><br>

Response

```javascript
Status: 200,
Content-Type: "application/json",
Body:
{
  "message": "Successfully deleted",
  "statusCode": 200
}
```

</details>

<br>

## Review images

<details>
<summary style="font-size: 18px; font-weight: 500">CREATE: Create an image for a review: <code>POST /api/reviews/:review_id/images</code></summary><br>

Request

```javascript
Content-Type: "application/json",
Body:
{
    "review_id": 3,
    "url": "my_tree.png",
}
```
---

Response

```javascript
Status: 201,
Content-Type: "application/json",
Body:
{
  "id": 1,
  "review_id": 3,
  "url": "my_tree.png",
}
```

</details>

<details>
<summary style="font-size: 18px; font-weight: 500">READ: Get images of a review: <code>GET /api/reviews/:review_id/images</code></summary><br>

Response

```javascript
Status: 200,
Content-Type: "application/json",
Body:
{
  "Images": [
    {
      "id": 1,
      "review_id": 1,
      "url": "tree_review_image.png",
    },
    {
      "id": 2,
      "review_id": 2,
      "url": "other_tree_review_image.png",
    },
  ]
}
```

</details>

<details>
<summary style="font-size: 18px; font-weight: 500">DELETE: Delete a review's image: <code>DELETE /api/review_images/:review_image_id</code></summary><br>

Response

```javascript
Status: 200,
Content-Type: "application/json",
Body:
{
  "message": "Successfully deleted",
  "statusCode": 200
}
```

</details>
