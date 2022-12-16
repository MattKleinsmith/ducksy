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
                <div className={styles.categoryWrapper}>
                    <a className={styles.imageWrapper} href='https://wwww.ducksy.onrender.com/listing/5'>
                        <img className={styles.categoryImage} src='/images/personalized_gifts.jpg' alt='img'></img>
                        <span className={styles.categoryName}>Personalized Gifts</span>
                    </a>
                    <a className={styles.imageWrapper} href='https://wwww.ducksy.onrender.com/listing/8'>
                        <span><img className={styles.categoryImage} src='/images/wedding.jpg' alt='img'></img></span>
                        <span className={styles.categoryName}>Wedding</span>
                    </a>
                    <a className={styles.imageWrapper} href='https://wwww.ducksy.onrender.com/listing/16'>
                        <span><img className={styles.categoryImage} src='/images/home_decor.jpg' alt='img'></img></span>
                        <span className={styles.categoryName}>Home Decor</span>
                    </a>
                    <a className={styles.imageWrapper} href='https://wwww.ducksy.onrender.com/listing/13'>
                        <span><img className={styles.categoryImage} src='/images/toy.jpg' alt='img'></img></span>
                        <span className={styles.categoryName}>Toy</span>
                    </a>
                    <a className={styles.imageWrapper} href='https://wwww.ducksy.onrender.com/listing/7'>
                        <span><img className={styles.categoryImage} src='/images/bag.jpg' alt='img'></img></span>
                        <span className={styles.categoryName}>Bag</span>
                    </a>
                    <a className={styles.imageWrapper} href='https://wwww.ducksy.onrender.com/listing/14'>
                        <span><img className={styles.categoryImage} src='/images/boyfriend.jpg' alt='img'></img></span>
                        <span className={styles.categoryName}>Boyfriend</span>
                    </a>
                </div>
            </div>
            <div className={styles.wrapper}>
                <div className={styles.recentViewed}>Recently viewed & more</div>
                <div className={styles.homepage}>
                    {products.map((product, i) =>
                        <div className={styles.productInfos} key={i}>
                            <NavLink to={`/listing/${product.id}`} style={{ textDecoration: 'none' }}>
                                <HomepageItem product={product} />
                            </NavLink>
                            <div className={styles.price}>
                                <span>$</span>{parseFloat(product.price).toFixed(2)}
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div >
    );
}
