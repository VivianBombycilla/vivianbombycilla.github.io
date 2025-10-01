const headerTemplate = document.createElement('template');

headerTemplate.innerHTML = `
    <style>
    ul {
        list-style: none;
        margin: 0;
        padding: 0;
    }

    li {
        display: inline;
    }
    </style>
    <header>
    <nav>
        <ul id="navigation-menu">
            <li>
                <a href="/">Home</a>
            </li>
            <li>
                <a href="/blog.html">Blog</a>
            </li>
            <li>
                <a href="/reading.html">Reading</a>
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
