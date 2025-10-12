const headerTemplate = document.createElement('template');

headerTemplate.innerHTML = `
    <style>
    ul.nav-menu {
        list-style: none;
        margin: 0;
        padding: 0;
        li {
            display: inline;
        }
    }
    </style>
    <header>
    <nav>
        <ul class="nav-menu">
            <li>
                <a href="/public/">Home</a>
            </li>
            <li>
                <a href="/public/blog.html">Blog</a>
            </li>
            <li>
                <a href="/public/reading.html">Reading</a>
            </li>
            <li>
                <a href="/public/games.html">Games</a>
            </li>
        </ul>
    </nav>
    </header>
`;

class Header extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        // Attach shadow root to custom component
        const shadowRoot = this.attachShadow({ mode: 'closed' });
        shadowRoot.appendChild(headerTemplate.content);
    }
}

customElements.define('header-component', Header);
