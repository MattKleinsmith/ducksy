import { NavLink, useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from 'react-redux';

import styles from "./Homepage.module.css";
import HomepageItem from "./HomepageItem/HomepageItem";
import { getProductsByCategory } from "../../store/productsBySearch";
import ProductGrid from "../ProductGrid/ProductGrid";
import HomepageFooter from "./HomepageFooter/HomepageFooter";

export default function Homepage() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const allproducts = useSelector(state => Object.values(state.products));
    const currentUser = useSelector(state => state.session.user);
    const products = allproducts.slice(0, 10);
    return (
        <>
            <div>
                <div className={styles.welcome}>
                    {currentUser ?
                        <div className={styles.welcomeText}>{`Welcome back, `}
                            <NavLink className={styles.NavlinkToPurchases} to='/your/purchases'>{currentUser.display_name}</NavLink>!</div>
                        :
                        <div className={styles.welcomeText}>Find things you'll love. Support independent sellers. Only on Ducksy.</div>}
                    <div className={styles.categoryWrapper}>
                        <div className={styles.imageWrapper}
                            onClick={async () => {
                                await dispatch(getProductsByCategory('personalized_gift'));
                                navigate('/category/personalized_gift');
                            }}
                        >
                            <img className={styles.categoryImage} src='/images/personalized_gifts.jpg' alt='img'></img>
                            <span className={styles.categoryName}>personalized gifts</span>
                        </div>
                        <div className={styles.imageWrapper}
                            onClick={async () => {
                                await dispatch(getProductsByCategory('wedding'));
                                navigate('/category/wedding');
                            }}
                        >
                            <span><img className={styles.categoryImage} src='/images/wedding.jpg' alt='img'></img></span>
                            <span className={styles.categoryName}>wedding</span>
                        </div>
                        <div className={styles.imageWrapper}
                            onClick={async () => {
                                await dispatch(getProductsByCategory('home_decor'));
                                navigate('/category/home_decor');
                            }}
                        >
                            <span><img className={styles.categoryImage} src='/images/home_decor.jpg' alt='img'></img></span>
                            <span className={styles.categoryName}>home decor</span>
                        </div>
                        <div className={styles.imageWrapper}
                            onClick={async () => {
                                await dispatch(getProductsByCategory('toy'));
                                navigate('/category/toy');
                            }}
                        >
                            <span><img className={styles.categoryImage} src='/images/toy.jpg' alt='img'></img></span>
                            <span className={styles.categoryName}>toy</span>
                        </div>
                        <div className={styles.imageWrapper}
                            onClick={async () => {
                                await dispatch(getProductsByCategory('bag'));
                                navigate('/category/bag');
                            }}
                        >
                            <span><img className={styles.categoryImage} src='/images/bag.jpg' alt='img'></img></span>
                            <span className={styles.categoryName}>bag</span>
                        </div>
                        <div className={styles.imageWrapper}
                            onClick={async () => {
                                await dispatch(getProductsByCategory('boyfriend'));
                                navigate('/category/boyfriend');
                            }}
                        >
                            <span><img className={styles.categoryImage} src='/images/boyfriend.jpg' alt='img'></img></span>
                            <span className={styles.categoryName}>boyfriend</span>
                        </div>
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
                                    <strong><span>$</span>{parseFloat(product.price).toFixed(2)}</strong>
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            </div >
            <ProductGrid isHomepage={true} />
            <HomepageFooter />
        </>
    );
}
