import { FaSearch } from "react-icons/fa";

export default function SearchBar() {
    return (
        <div className="search-bar">
            <input type="text" placeholder="Search..." />
            <button className="search-button" onClick={() => {
                window.alert('Feature coming soon!');
            }}>
                <FaSearch />
            </button>
        </div>
    )
}
