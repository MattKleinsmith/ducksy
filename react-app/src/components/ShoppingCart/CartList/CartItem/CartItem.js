import { deleteItemFromCart } from '../../../../store/shoppingCart';
import { useDispatch, useSelector } from 'react-redux';
import './CartItem.css';
import ItemQuantity from './ItemQuantity/ItemQuantity';

export default function CartItem({ product, quantity }) {
    const dispatch = useDispatch()
    const user = useSelector(state => state.session.user)

    return (
        <div className='cartItem'>
            <div className="cart_seller_info">
                <div className="seller_profile_picture">
                    D
                </div>
                <div>{product.seller.display_name}</div>
            </div>

            <div className="cart_product_grid">
                <div className="cart_product_image">
                    <img src={product.preview_image} alt={product.name}></img>
                </div>
                <div className="cart_grid_middle_ele">
                    <div>
                        {product.name}
                    </div>
                    <div>
                        <button
                            onClick={() => dispatch(deleteItemFromCart(product, user))}
                        >Remove</button>
                    </div>
                </div>
                <ItemQuantity initialQuantity={quantity} user={user} product={product} />
            </div>
        </div >
    )
}
