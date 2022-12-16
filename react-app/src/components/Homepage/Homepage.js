import { NavLink } from "react-router-dom";
import { useSelector } from 'react-redux';

import styles from "./Homepage.module.css";
import HomepageItem from "./HomepageItem/HomepageItem";
// import { clearProductDetails } from "../../store/productDetails";

export default function Homepage() {
    const allproducts = useSelector(state => Object.values(state.products));
    const currentUser = useSelector(state => state.session.user);
    const products = allproducts.slice(0, 10);
    return (
        <div>
            <div className={styles.welcome}>{currentUser ?
                <div>Welcome back, {currentUser.display_name}</div> :
                <div>Find things you'll love. Support independent sellers. Only on Ducksy.</div>}
                <div>
                    <div>
                        <img href='' alt=''></img>
                        <div>Gift</div>
                    </div>
                    <div>Wedding</div>
                    <div>Personalized Gifts</div>
                    <div>Home Decor</div>
                    <div>Bag</div>
                    <div>Boyfriend</div>
                </div>
            </div>
            <div className={styles.welcome}></div>
            <div className={styles.wrapper}>
                <div className={styles.recentViewed}>Recently viewed & more</div>
                <div className={styles.homepage}>
                    {products.map((product, i) =>
                        <div className={styles.productInfos}>
                            <NavLink key={i} to={`/listing/${product.id}`} style={{ textDecoration: 'none' }}>
                                <HomepageItem product={product} />
                            </NavLink>
                            <div className={styles.price}>
                                <span>$</span>{parseFloat(product.price).toFixed(2)}
                            </div>
                        </div>
                    )}
                </div >
            </div>
        </div >
    );
}
