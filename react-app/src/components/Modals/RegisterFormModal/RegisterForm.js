import styles from './RegisterForm.module.css';
import { useState } from "react";
import { useDispatch } from "react-redux";
import * as sessionActions from "../../../store/session";
import { setRegisterModal } from "../../../store/ui";

export default function RegisterForm() {
    const dispatch = useDispatch();
    const [email, setEmail] = useState("");
    const [display_name, setDisplay_Name] = useState("");
    const [password, setPassword] = useState("");
    const [errors, setErrors] = useState([]);

    const handleSubmit = (e) => {
        e.preventDefault();
        setErrors([]);
        return dispatch(sessionActions.register({ email, display_name, password }))
            .then(() => dispatch(setRegisterModal(false)))
            .catch(e => {
                const errors = Object.entries(e.errors).map(([errorField, errorMessage]) => `${errorField}: ${errorMessage}`);
                setErrors(errors);
            });
    };

    return (
        <form className={styles.form} onSubmit={handleSubmit}>
            <div className={styles.header}>Create your account</div>
            <div className={styles.tagline}>Registration is easy.</div>
            {errors.length > 0 && <ul className={styles.formErrors}>
                {errors.map((error, i) => <li key={i}>{error}</li>)}
            </ul>}
            <label className={styles.label}>
                Email address <span style={{ color: "#A61A2E" }}>*</span><br />
                <input
                    className="field"
                    type="text"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                />
            </label>
            <label className={styles.label}>
                First name <span style={{ color: "#A61A2E" }}>*</span><br />
                <input
                    type="text"
                    value={display_name}
                    onChange={(e) => setDisplay_Name(e.target.value)}
                    required
                />
            </label>
            <label className={styles.label}>
                Password <span style={{ color: "#A61A2E" }}>*</span><br />
                <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
            </label>
            <button type="submit" className={`${styles.button} ${email && display_name && password ? styles.buttonReady : styles.buttonNotReady}`}>Register</button>
        </form>
    );
}
