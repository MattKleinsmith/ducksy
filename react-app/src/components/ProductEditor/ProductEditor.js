import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate, useParams } from "react-router-dom";
import { putProduct, postProduct } from "../../store/products";
import { postProductImage } from "../../store/products";

import styles from "./ProductEditor.module.css";
import footerStyles from "./ProductEditorFooter/ProductEditorFooter.module.css"

export default function ProductEditor() {
    const navigate = useNavigate();
    const { productId } = useParams();
    const dispatch = useDispatch();
    const product = useSelector(state => state.products)[productId]

    const [image, setImage] = useState(null);
    const [preview, setPreview] = useState(true);
    const [imageErrors, setImageErrors] = useState([]);

    const [name, setName] = useState(product?.name || "");
    const [description, setDescription] = useState(product?.description || "");
    const [price, setPrice] = useState(product?.price || 0);
    const [errors, setErrors] = useState([]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setErrors([]);
        const body = { name, description, price };
        if (image || product?.preview_image) {
            try {
                const productThunkAction = product ? putProduct(productId, body) : postProduct(body)
                const newProductId = await dispatch(productThunkAction)
                try {
                    setImageErrors([]);
                    if (image)
                        dispatch(postProductImage(newProductId ? newProductId : productId, image, preview))
                    // dispatch(setDataLoadingModal(true));
                    navigate("/your/shop");
                }
                catch (responseBody) {
                    setImageErrors(Object.values(responseBody.errors))
                }
            }
            catch (responseBody) {
                const errors = Object.entries(responseBody.errors).map(([errorField, errorMessage]) => `${errorField}: ${errorMessage}`)
                setErrors(errors);
            }
        }
        else {
            setImageErrors(["Please upload an image for the product listing"])
        }

    };

    const handleImageChange = (e) => {
        const file = e.target.files[0];
        setImage(file)
        const reader = new FileReader();
        reader.onload = function (e) {
            document.querySelector("#ProductEditorImage").src = e.target.result;
        }
        reader.readAsDataURL(file);
    }

    return (
        <div className={styles.ProductEditorWrapper}>
            <div className={styles.ProductEditor}>
                <h1>{productId ? "Editing" : "Creating"} a listing {productId}</h1>
                <p>Add some photos and details about your item. Fill out what you can for now—you’ll be able to edit this later.</p>

                <form className={styles.form}>
                    <div className={styles.formForImage}>
                        {imageErrors.length > 0 && <ul className="formErrors">
                            {imageErrors.map((error, i) => <li key={i} style={{ color: "red" }}>{error}</li>)}
                        </ul>}
                        <div className={styles.formSectionName}>Photos</div>
                        <p>Add as many as you can so buyers can see every detail.</p>

                        <div className={styles.formImageGrid}>
                            <div className={styles.formImageTips}>
                                <h3>Photos*</h3>
                                <p>
                                    Use up to ten photos to show your item's most important qualities.
                                </p>
                                <p>Tips</p>
                                <ul>
                                    <li>Use natural light and no flash.</li>
                                    <li>Include a common object for scale.</li>
                                    <li>Show the item being held, worn, or used.</li>
                                    <li>Shoot against a clean, simple background.</li>
                                    <li>Add photos to your variations so buyers can see all their options.</li>
                                </ul>

                            </div>
                            <div className={styles.formImageInput}>

                                <div>
                                    <label>Add a photo*{" "}
                                        <input
                                            type="file"
                                            name="image"
                                            accept="image/png, image/jpeg"
                                            onChange={handleImageChange}
                                        />
                                    </label>
                                </div>
                                <label>Is this a preview image?{" "}
                                    <input
                                        type="checkbox"
                                        name="preview"
                                        className={styles.checkbox}
                                        checked={preview}
                                        onChange={() => setPreview(!preview)}
                                    />
                                </label>
                                <img id="ProductEditorImage" className={styles.image} src={product?.preview_image} alt={product?.preview_image} />
                            </div>
                        </div>
                    </div>

                    <div className={styles.formForDetails}>
                        <div className={styles.formSectionName}>Listing details</div>
                        <p>Tell the world all about your item and why they’ll love it.</p>

                        {errors.length > 0 && <ul className="formErrors">
                            {errors.map((error, i) => <li key={i} style={{ color: "red" }}>{error}</li>)}
                        </ul>}
                        <div className={styles.formDetailsGrid}>
                            <div>
                                <label htmlFor="name">Name*</label>
                                <p>Include keywords that buyers would use to search for your item.</p>
                            </div>
                            <div>
                                <input
                                    type="text"
                                    value={name}
                                    id="name"
                                    onChange={e => setName(e.target.value)}
                                />
                            </div>
                            <div>

                                <label htmlFor="description">Description*</label>
                                <p>Start with a brief overview that describes your item’s finest features. Shoppers will only see the first few lines of your description at first, so make it count!</p>
                                <p>Not sure what else to say? Shoppers also like hearing about your process, and the story behind this item.</p>
                            </div>
                            <div>
                                <textarea
                                    value={description}
                                    id="description"
                                    onChange={e => setDescription(e.target.value)}
                                />
                            </div>
                        </div>

                    </div>

                    <div className={styles.formforPrice}>
                        <div className={styles.formSectionName}>Price</div>

                        <div className={styles.formPriceGrid}>
                            <div>
                                <label>Price*</label>
                                <p>Remember to factor in the costs of materials, labor, and other business expenses. If you offer free shipping, make sure to include the cost of shipping so it doesn't eat into your profits.</p>
                            </div>
                            <div>
                                <input
                                    type="number"
                                    value={price}
                                    onChange={e => setPrice(e.target.value)}
                                />
                            </div>

                        </div>

                    </div>
                </form>
            </div>
            <div className={footerStyles.wrapper}>
                <div className={footerStyles.line} />
                <div className={footerStyles.footer}>
                    <div className={`${footerStyles.button} ${footerStyles.cancel}`} onClick={() => navigate("/your/shop")}>Cancel</div>
                    <div className={`${footerStyles.button} ${footerStyles.saveAndContinue}`} onClick={handleSubmit}>Save and continue</div>
                </div>
            </div>
        </div>
    );
}
