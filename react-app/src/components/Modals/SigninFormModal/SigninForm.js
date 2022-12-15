import './SigninForm.css';
import { useState } from "react";
import { useDispatch } from "react-redux";
import * as sessionActions from "../../../store/session";
import { setSigninModal, setRegisterModal } from "../../../store/ui";

export default function SigninForm() {
    const dispatch = useDispatch();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [errors, setErrors] = useState([]);

    const handleSubmit = (e) => {
        e.preventDefault();
        setErrors([]);
        return dispatch(sessionActions.signIn({ email, password }))
            .then(() => dispatch(setSigninModal(false)))
            .catch(errors => {
                setErrors(Object.values(errors.errors))
            });
    };

    return (
        <form className="signinForm" onSubmit={handleSubmit}>
            <div className="signinHeader">
                <div>Sign in</div>
            </div>
            <div className="signInFormRegisterButton" onClick={() => {
                dispatch(setRegisterModal(true));
                dispatch(setSigninModal(false));
            }}>Register</div>
            {errors.length > 0 && <ul className="formErrors">
                {errors.map((error, idx) => <li key={idx}>{error}</li>)}
            </ul>}
            <label>
                Email address <br />
                <input
                    className="field"
                    type="text"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                />
            </label>
            <label>
                Password <br />
                <input
                    className="field"
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
            </label>

            <button type="submit" className="signinButton">Sign in</button>

            <button type="submit" className="demoButton" onClick={() => {
                setEmail("email@email.com");
                setPassword("password");
            }}>Log in as demo user: Anna</button>

            <button type="submit" className="demoButton" onClick={() => {
                setEmail("email2@email.com");
                setPassword("password");
            }}>Log in as demo user: Brian</button>
        </form>
    );
}
