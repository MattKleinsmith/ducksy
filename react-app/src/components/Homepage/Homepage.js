import { NavLink, useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from 'react-redux';

import styles from "./Homepage.module.css";
import HomepageItem from "./HomepageItem/HomepageItem";
import { getProductsByCategory } from "../../store/productsBySearch";
import ProductGrid from "../ProductGrid/ProductGrid";

export default function Homepage() {
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const allProducts = useSelector(state => state.products);
    const currentUser = useSelector(state => state.session.user);
    const products = Object.values(allProducts).slice(0, 8);
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
                            <img className={styles.categoryImage} src={`${allProducts[27]?.product_images[0].url}`} alt=''></img>
                            <span className={styles.categoryName}>Personalized Gifts</span>
                        </div>
                        <div className={styles.imageWrapper}
                            onClick={async () => {
                                await dispatch(getProductsByCategory('wedding'));
                                navigate('/category/wedding');
                            }}
                        >
                            <span><img className={styles.categoryImage} src={`${allProducts[28]?.product_images[0].url}`} alt=''></img></span>
                            <span className={styles.categoryName}>Wedding</span>
                        </div>
                        <div className={styles.imageWrapper}
                            onClick={async () => {
                                await dispatch(getProductsByCategory('home_decor'));
                                navigate('/category/home_decor');
                            }}
                        >
                            <span><img className={styles.categoryImage} src={`${allProducts[11]?.product_images[0].url}`} alt=''></img></span>
                            <span className={styles.categoryName}>Home decor</span>
                        </div>
                        <div className={styles.imageWrapper}
                            onClick={async () => {
                                await dispatch(getProductsByCategory('toy'));
                                navigate('/category/toy');
                            }}
                        >
                            <span><img className={styles.categoryImage} src={`${allProducts[14]?.product_images[0].url}`} alt=''></img></span>
                            <span className={styles.categoryName}>Toy</span>
                        </div>
                        <div className={styles.imageWrapper}
                            onClick={async () => {
                                await dispatch(getProductsByCategory('bag'));
                                navigate('/category/bag');
                            }}
                        >
                            <span><img className={styles.categoryImage} src={`${allProducts[9]?.product_images[0].url}`} alt=''></img></span>
                            <span className={styles.categoryName}>Bag</span>
                        </div>
                        <div className={styles.imageWrapper}
                            onClick={async () => {
                                await dispatch(getProductsByCategory('boyfriend'));
                                navigate('/category/boyfriend');
                            }}
                        >
                            <span><img className={styles.categoryImage} src={`${allProducts[15]?.product_images[0].url}`} alt=''></img></span>
                            <span className={styles.categoryName}>Boyfriend</span>
                        </div>
                    </div>
                </div>
                <div className={styles.wrapper}>
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
                <div className={styles.popularGiftWrapper}>
                    <div className={styles.popularGift}>Popular gifts right now</div>
                    <ProductGrid isHomepage={true} />
                </div>
            </div >
        </>
    );
}
