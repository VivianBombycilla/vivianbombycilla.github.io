const headerTemplate = document.createElement('template');

headerTemplate.innerHTML = `
    <style>
    ul.nav-menu {
        margin: 0;
        padding: 0;
        height: 2em;
        transform: rotate(-90deg) translateY(100%);
        transform-origin: bottom left;
        li {
            // list-style-image: url("components/bullet.svg");
            width: max-content;
            margin: 0;
            padding: 0;
            padding-left: 0.25em;
            transform: rotate(30deg);
            transform-origin: bottom left;
            font-size: 12pt;
        }
        li::marker {
            content: url("/components/bullet.svg");
        }
        li:before {
            background-color: #000;
            width: 2.7px;
            content: '';
            position: fixed;
            top: 0px;
            bottom: 0px;
            left: -0.2px;
            transform: rotate(-30deg);
            transform-origin: bottom left;
            
        }
        li:first-child:before {
            top: 11px;
        }
        li:last-child:before {
            transform: rotate(-30deg) translateY(-10px);
        }
        a {
            color: blue;
        }
    }
    </style>
    <header>
    <nav>
        <ul class="nav-menu">
            <li>
                <a href="/">Home</a>
            </li>
            <li>
                <a href="/blog.html">Website</a>
            </li>
            <li>
                <a href="/reading.html">Reading</a>
            </li>
            <li>
                <a href="/games.html">Games</a>
            </li>
            <li>
                <a href="/fun.html">Fun</a>
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
