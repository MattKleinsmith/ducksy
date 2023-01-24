import { useEffect } from "react"
import { useDispatch } from "react-redux";
import { setDataLoadingModal } from "../../../store/ui";
import styles from './DataLoadingBuffer.module.css'

export default function DataLoadingBuffer() {
    const dispatch = useDispatch();
    useEffect(() => {
        return () => {
            dispatch(setDataLoadingModal(false));
        }
    }, [dispatch]);

    return (
        <div className={styles.DataLoadingBuffer}>
            <img alt="duck loading" src="/images/duck.gif"></img>
            <div>Duck loading your shopping cart</div>
        </div>
    )
}
