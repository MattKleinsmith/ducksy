import styles from "./RightHeader.module.css";
import { useDispatch, useSelector } from "react-redux";
import ProfileButton from "./ProfileButton/ProfileButton";
import CartButton from "./CartButton/CartButton";
import ShopButton from "./ShopButton/ShopButton";
import { setSigninModal } from "../../../store/ui";

export default function RightHeader() {
    const session = useSelector(state => state.session);
    const dispatch = useDispatch();
    return <span>
        {<div className={styles.wrapper}>
            {session.user && <ShopButton />}
            {!session.user && <div className={styles.signInWrapper}><div className={styles.signIn} onClick={() => dispatch(setSigninModal(true))}>Sign in</div></div>}
            {session.user && <ProfileButton />}
            <CartButton />
        </div>}
    </span>
}
