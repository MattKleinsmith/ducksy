import styles from './OrderConfirmation.module.css'
import { useEffect } from 'react'
import { useNavigate, useParams } from 'react-router'
import { NavLink } from 'react-router-dom'

export default function OrderConfirmation() {
    const { orderId } = useParams()
    const navigate = useNavigate()
    useEffect(() => {
        const timeout = setTimeout(() => navigate('/'), 5000);
        return () => clearTimeout(timeout);
    })

    return (
        <div className={styles.OrderConfirmation}>
            <div className={styles.confirmation_message}>
                <h1>We have received your order!</h1>
            </div>
            <div className={styles.confirmation_order_id}>
                <h2>Order number: {orderId}</h2>

            </div>
            <div>
                <NavLink to='/'>You will be redirected to home page in 5 seconds...</NavLink>

            </div>
        </div>
    )
}
