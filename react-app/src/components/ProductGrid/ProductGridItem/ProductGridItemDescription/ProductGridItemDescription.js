import "./ProductGridItemDescription.css"

export default function ProductGridItemDescription({ product }) {
    return (
        <div className="ProductGridItemDescription">
            <div className="ProductGridItemDescriptionName">{product.name}</div>
            {product.shop_rating &&
                <div className="ProductGridItemStarRating">
                    <i className="fa-solid fa-star ProductGridItemStar" />
                    <i className="fa-solid fa-star ProductGridItemStar" />
                    <i className="fa-solid fa-star ProductGridItemStar" />
                    <i className="fa-solid fa-star ProductGridItemStar" />
                    <i className="fa-solid fa-star ProductGridItemStar" />
                    ({product.num_shop_ratings})
                </div>
            }
            <div className="ProductGridItemPrice"><strong>${product.price}</strong></div>
        </div>
    );
}
