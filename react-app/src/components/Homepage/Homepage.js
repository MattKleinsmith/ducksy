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
                    <div className={styles.imageWrapper}>
                        <img className={styles.categoryImage} src='https://i.etsystatic.com/17766621/r/il/16e3f0/4236608158/il_794xN.4236608158_aztc.jpg' alt='img'></img>
                        <div className={styles.categoryName}>Personalized Gifts</div>
                    </div>
                    <div className={styles.imageWrapper}>
                        <img className={styles.categoryImage} src='https://i.etsystatic.com/8617622/r/il/0c6972/2264040092/il_794xN.2264040092_5oim.jpg' alt='img'></img>
                        <div className={styles.categoryName}>Wedding</div>
                    </div>
                    <div className={styles.imageWrapper}>
                        <img className={styles.categoryImage} src='https://i.etsystatic.com/27235619/r/il/b029b4/2847834009/il_794xN.2847834009_nd9k.jpg' alt='img'></img>
                        <div className={styles.categoryName}>Home Decor</div>
                    </div>
                    <div className={styles.imageWrapper}>
                        <img className={styles.categoryImage} src='https://i.etsystatic.com/17305851/r/il/95b009/3398360096/il_794xN.3398360096_rpcp.jpg' alt='img'></img>
                        <div className={styles.categoryName}>Toy</div>
                    </div>
                    <div className={styles.imageWrapper}>
                        <img className={styles.categoryImage} src='https://i.etsystatic.com/21515874/r/il/70440b/2916023872/il_794xN.2916023872_agns.jpg' alt='img'></img>
                        <div className={styles.categoryName}>Bag</div>
                    </div>
                    <div className={styles.imageWrapper}>
                        <img className={styles.categoryImage} src='https://i.etsystatic.com/20811748/r/il/824d8a/3906405268/il_794xN.3906405268_aubi.jpg' alt='img'></img>
                        <div className={styles.categoryName}>Boyfriend</div>
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
                                <span>$</span>{parseFloat(product.price).toFixed(2)}
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}
