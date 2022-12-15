import { NavLink } from "react-router-dom";
import { useSelector } from 'react-redux';

import styles from "./Homepage.module.css";
import HomepageItem from "./HomepageItem/HomepageItem";
// import { clearProductDetails } from "../../store/productDetails";

export default function Homepage() {
    const products = useSelector(state => Object.values(state.products));
    const currentUser = useSelector(state => state.session.user);
    return (
        <div>
            <div className={styles.welcome}>{currentUser ?
                <div>`Welcome back, ${currentUser.display_name}`</div> :
                <div>Find things you'll love. Support independent sellers. Only on Ducksy.</div>}
            </div>
            <div className={styles.welcome}></div>
            <div className={styles.wrapper}>
                <div>Recently viewed & more</div>
                <div className={styles.homepage}>
                    {products.map((product, i) =>
                        <div className={styles.productInfos}>
                            <NavLink key={i} to={`/listing/${product.id}`} style={{ textDecoration: 'none' }}>
                                <HomepageItem product={product} />
                            </NavLink>
                            <div>
                                <span>$</span>{parseFloat(product.price).toFixed(2)}
                            </div>
                        </div>
                    )}
                </div >
            </div>
        </div >
    );
}
