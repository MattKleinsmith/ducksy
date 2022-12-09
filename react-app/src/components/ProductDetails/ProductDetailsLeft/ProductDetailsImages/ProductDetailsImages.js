import "./ProductDetailsImages.css"

export default function ProductDetailsImages({ product }) {
    return (
        <div className="ProductDetailsImagesWrapper">
            <div className="ProductDetailsImages">
                <img src={product.preview_image} alt="ProductDetailsImages" />
            </div>
        </div>
    );
}
