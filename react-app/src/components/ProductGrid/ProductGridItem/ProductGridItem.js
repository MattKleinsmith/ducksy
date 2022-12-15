import "./ProductGridItem.css"
import ProductGridItemDescription from "./ProductGridItemDescription/ProductGridItemDescription";

export default function ProductGridItem({ product }) {
    return (
        <div className="ProductGridItem">
            <img src={product.preview_image} alt={product.preview_image} onError={(e) => { e.target.src = "/placeholder.png" }} />
            <ProductGridItemDescription product={product} />
        </div>
    );
}
