import { FaArrowLeft } from "react-icons/fa6";

import './Page404.css';

export default function Page404() {
    return (
        <div className="page404">
            <h1>Uh oh!</h1>
            <span>
                Sorry, the page you were looking for was not found.
            </span>
            <button>
                <FaArrowLeft />
                Go back to Etsy.com
            </button>
        </div>
    );
}