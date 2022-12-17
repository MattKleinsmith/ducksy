import "./ProductGridItemDescription.css";

export default function ProductGridItemDescription({ product }) {
    return (
        <div className="ProductGridItemDescription">
            <div className="ProductGridItemDescriptionName">{product.name}</div>
            {product.seller_rating &&
                <div className="ProductGridItemStarRating">
                    <i className="fa-solid fa-star ProductGridItemStar" />
                    <i className="fa-solid fa-star ProductGridItemStar" />
                    <i className="fa-solid fa-star ProductGridItemStar" />
                    <i className="fa-solid fa-star ProductGridItemStar" />
                    <i className="fa-solid fa-star ProductGridItemStar" />
                    ({product.num_seller_ratings})
                </div>
            }
            <div className="ProductGridItemPrice"><strong>${parseFloat(product.price).toFixed(2)}</strong></div>
        </div>
    );
}
