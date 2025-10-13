const headerTemplate = document.createElement('template');

headerTemplate.innerHTML = `
    <style>
    ul.nav-menu {
        padding: 0;
        height: 2em;
        transform: rotate(-90deg) translateY(100%);
        transform-origin: bottom left;
        li {
            width: max-content;
            margin: 0;
            padding: 0;
            transform: rotate(30deg);
            transform-origin: bottom left;
            font-size: 12pt;
        }
        li::marker {
            font-size: 17pt
        }
        li:before {
            background-color: #000;
            width: 2px;
            content: '';
            position: absolute;
            top: 0px;
            bottom: 0px;
            left: -7.93px;
            transform: rotate(-30deg);
            transform-origin: bottom left;
            
        }
        li:first-child:before {
            top: 13px;
        }
        li:last-child:before {
            transform: rotate(-30deg) translateY(-13px);
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
                <a href="/blog.html">Blog</a>
            </li>
            <li>
                <a href="/reading.html">Reading</a>
            </li>
            <li>
                <a href="/games.html">Games</a>
            </li>
            <li>
                <a href="/tools.html">Tools</a>
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
