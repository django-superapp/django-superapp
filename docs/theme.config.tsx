import { useRouter } from 'next/router'
import type { DocsThemeConfig } from 'nextra-theme-docs'
import { useConfig } from 'nextra-theme-docs'

const logo = (
  <svg
    height="50"
    viewBox="0 0 548 180"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    style={{marginTop: "10px", color: "#020D37"}}
    className={'logo'}
  >
      <path
          d="M43.832 94.3633C43.832 93.1914 43.4609 92.1562 42.7188 91.2578C42.0156 90.3594 40.7266 89.5391 38.8516 88.7969C37.0156 88.0547 34.418 87.3125 31.0586 86.5703C27.8945 85.9062 24.9453 85.0469 22.2109 83.9922C19.4766 82.8984 17.0938 81.5898 15.0625 80.0664C13.0312 78.5039 11.4492 76.668 10.3164 74.5586C9.18359 72.4102 8.61719 69.9688 8.61719 67.2344C8.61719 64.5781 9.18359 62.0586 10.3164 59.6758C11.4883 57.293 13.168 55.1836 15.3555 53.3477C17.582 51.5117 20.2773 50.0664 23.4414 49.0117C26.6445 47.957 30.2773 47.4297 34.3398 47.4297C39.9258 47.4297 44.75 48.3086 48.8125 50.0664C52.875 51.7852 56 54.207 58.1875 57.332C60.375 60.418 61.4688 63.9531 61.4688 67.9375H43.1875C43.1875 66.2969 42.875 64.8711 42.25 63.6602C41.625 62.4492 40.668 61.5117 39.3789 60.8477C38.0898 60.1445 36.3906 59.793 34.2812 59.793C32.6406 59.793 31.1953 60.0859 29.9453 60.6719C28.7344 61.2188 27.7773 61.9805 27.0742 62.957C26.4102 63.9336 26.0781 65.0664 26.0781 66.3555C26.0781 67.2539 26.2734 68.0742 26.6641 68.8164C27.0938 69.5195 27.7383 70.1836 28.5977 70.8086C29.4961 71.3945 30.6484 71.9219 32.0547 72.3906C33.5 72.8594 35.2578 73.3086 37.3281 73.7383C41.7422 74.5586 45.7656 75.7109 49.3984 77.1953C53.0703 78.6797 56 80.7305 58.1875 83.3477C60.4141 85.9648 61.5273 89.4219 61.5273 93.7188C61.5273 96.5312 60.8828 99.1094 59.5938 101.453C58.3438 103.797 56.5273 105.848 54.1445 107.605C51.7617 109.363 48.9102 110.73 45.5898 111.707C42.2695 112.684 38.5195 113.172 34.3398 113.172C28.3633 113.172 23.3047 112.098 19.1641 109.949C15.0234 107.801 11.8984 105.105 9.78906 101.863C7.71875 98.582 6.68359 95.2227 6.68359 91.7852H23.8516C23.9297 93.8945 24.457 95.6133 25.4336 96.9414C26.4492 98.2695 27.7578 99.2461 29.3594 99.8711C30.9609 100.457 32.7578 100.75 34.75 100.75C36.7422 100.75 38.4023 100.477 39.7305 99.9297C41.0586 99.3828 42.0742 98.6406 42.7773 97.7031C43.4805 96.7266 43.832 95.6133 43.832 94.3633ZM108.93 96.707V48.6016H127.328V112H110.102L108.93 96.707ZM110.863 83.7578L115.902 83.6406C115.902 87.8984 115.395 91.8242 114.379 95.418C113.402 99.0117 111.918 102.137 109.926 104.793C107.973 107.449 105.531 109.52 102.602 111.004C99.7109 112.449 96.332 113.172 92.4648 113.172C89.3398 113.172 86.4688 112.742 83.8516 111.883C81.2734 110.984 79.0469 109.598 77.1719 107.723C75.2969 105.809 73.8516 103.367 72.8359 100.398C71.8203 97.3906 71.3125 93.7969 71.3125 89.6172V48.6016H89.5938V89.7344C89.5938 91.375 89.7891 92.7812 90.1797 93.9531C90.6094 95.0859 91.1758 96.0234 91.8789 96.7656C92.6211 97.5078 93.5195 98.0547 94.5742 98.4062C95.668 98.7578 96.8594 98.9336 98.1484 98.9336C101.391 98.9336 103.93 98.2695 105.766 96.9414C107.641 95.5742 108.949 93.7578 109.691 91.4922C110.473 89.1875 110.863 86.6094 110.863 83.7578ZM157.562 60.7891V136.375H139.281V48.6016H156.332L157.562 60.7891ZM197.113 79.5977V80.8281C197.113 85.4375 196.586 89.7148 195.531 93.6602C194.477 97.5664 192.895 100.984 190.785 103.914C188.715 106.844 186.156 109.129 183.109 110.77C180.062 112.371 176.527 113.172 172.504 113.172C168.676 113.172 165.355 112.371 162.543 110.77C159.77 109.129 157.426 106.863 155.512 103.973C153.637 101.043 152.113 97.7031 150.941 93.9531C149.809 90.1641 148.93 86.1211 148.305 81.8242V79.4219C148.93 74.8516 149.828 70.6133 151 66.707C152.172 62.8008 153.695 59.4219 155.57 56.5703C157.445 53.6797 159.77 51.4336 162.543 49.832C165.316 48.2305 168.617 47.4297 172.445 47.4297C176.43 47.4297 179.965 48.1914 183.051 49.7148C186.137 51.2383 188.715 53.4258 190.785 56.2773C192.895 59.0898 194.477 62.4688 195.531 66.4141C196.586 70.3594 197.113 74.7539 197.113 79.5977ZM178.773 80.8281V79.5977C178.773 77.0195 178.578 74.6562 178.188 72.5078C177.797 70.3203 177.172 68.4258 176.312 66.8242C175.453 65.1836 174.32 63.9141 172.914 63.0156C171.508 62.1172 169.789 61.668 167.758 61.668C165.57 61.668 163.715 62.0195 162.191 62.7227C160.668 63.4258 159.438 64.4609 158.5 65.8281C157.562 67.1562 156.879 68.7969 156.449 70.75C156.059 72.7031 155.844 74.9297 155.805 77.4297V83.875C155.844 86.8047 156.254 89.4219 157.035 91.7266C157.855 93.9922 159.125 95.7695 160.844 97.0586C162.602 98.3086 164.945 98.9336 167.875 98.9336C169.945 98.9336 171.664 98.4844 173.031 97.5859C174.438 96.6484 175.551 95.3398 176.371 93.6602C177.23 91.9805 177.836 90.0469 178.188 87.8594C178.578 85.6719 178.773 83.3281 178.773 80.8281ZM236.723 113.172C231.684 113.172 227.172 112.371 223.188 110.77C219.203 109.168 215.824 106.961 213.051 104.148C210.316 101.297 208.227 98.0156 206.781 94.3047C205.336 90.5938 204.613 86.6289 204.613 82.4102V80.1836C204.613 75.457 205.277 71.1016 206.605 67.1172C207.934 63.1328 209.867 59.6758 212.406 56.7461C214.984 53.7773 218.148 51.4922 221.898 49.8906C225.648 48.25 229.926 47.4297 234.73 47.4297C239.223 47.4297 243.227 48.1719 246.742 49.6562C250.258 51.1016 253.227 53.1914 255.648 55.9258C258.07 58.6211 259.906 61.8828 261.156 65.7109C262.445 69.5 263.09 73.7578 263.09 78.4844V85.9844H211.996V74.207H245.16V72.8008C245.16 70.5742 244.75 68.6211 243.93 66.9414C243.148 65.2617 241.977 63.9727 240.414 63.0742C238.891 62.1367 236.957 61.668 234.613 61.668C232.387 61.668 230.531 62.1367 229.047 63.0742C227.562 64.0117 226.371 65.3398 225.473 67.0586C224.613 68.7383 223.988 70.7109 223.598 72.9766C223.207 75.2031 223.012 77.6055 223.012 80.1836V82.4102C223.012 84.8711 223.344 87.1172 224.008 89.1484C224.672 91.1797 225.648 92.918 226.938 94.3633C228.227 95.8086 229.789 96.9414 231.625 97.7617C233.461 98.582 235.551 98.9922 237.895 98.9922C240.785 98.9922 243.539 98.4453 246.156 97.3516C248.773 96.2188 251.039 94.4609 252.953 92.0781L261.508 101.863C260.219 103.738 258.402 105.555 256.059 107.312C253.754 109.031 250.98 110.438 247.738 111.531C244.496 112.625 240.824 113.172 236.723 113.172ZM290.336 63.3672V112H272.055V48.6016H289.223L290.336 63.3672ZM309.262 48.1328L308.969 65.1836C308.188 65.0664 307.172 64.9688 305.922 64.8906C304.672 64.7734 303.598 64.7148 302.699 64.7148C300.355 64.7148 298.324 65.0078 296.605 65.5938C294.926 66.1406 293.52 66.9609 292.387 68.0547C291.293 69.1484 290.473 70.5156 289.926 72.1562C289.379 73.7578 289.105 75.6133 289.105 77.7227L285.648 76.0234C285.648 71.8438 286.059 68.0156 286.879 64.5391C287.699 61.0625 288.891 58.0547 290.453 55.5156C292.016 52.9375 293.93 50.9453 296.195 49.5391C298.461 48.1328 301.039 47.4297 303.93 47.4297C304.867 47.4297 305.824 47.4883 306.801 47.6055C307.777 47.7227 308.598 47.8984 309.262 48.1328ZM348.461 96.8828V69.6953C348.461 67.7812 348.168 66.1406 347.582 64.7734C346.996 63.4062 346.078 62.332 344.828 61.5508C343.578 60.7695 341.957 60.3789 339.965 60.3789C338.285 60.3789 336.82 60.6719 335.57 61.2578C334.359 61.8438 333.422 62.6836 332.758 63.7773C332.133 64.8711 331.82 66.2188 331.82 67.8203H313.539C313.539 64.9688 314.184 62.3125 315.473 59.8516C316.762 57.3906 318.598 55.2227 320.98 53.3477C323.402 51.4727 326.293 50.0273 329.652 49.0117C333.012 47.957 336.781 47.4297 340.961 47.4297C345.922 47.4297 350.336 48.2695 354.203 49.9492C358.109 51.5898 361.195 54.0703 363.461 57.3906C365.727 60.6719 366.859 64.8125 366.859 69.8125V96.3555C366.859 100.184 367.074 103.191 367.504 105.379C367.973 107.527 368.637 109.402 369.496 111.004V112H351.039C350.18 110.164 349.535 107.898 349.105 105.203C348.676 102.469 348.461 99.6953 348.461 96.8828ZM350.746 73.3281L350.863 83.4062H341.781C339.75 83.4062 337.992 83.6602 336.508 84.168C335.062 84.6758 333.891 85.3789 332.992 86.2773C332.094 87.1367 331.43 88.1523 331 89.3242C330.609 90.457 330.414 91.707 330.414 93.0742C330.414 94.3633 330.727 95.5352 331.352 96.5898C331.977 97.6055 332.836 98.4062 333.93 98.9922C335.023 99.5781 336.293 99.8711 337.738 99.8711C340.121 99.8711 342.152 99.4023 343.832 98.4648C345.551 97.5273 346.879 96.3945 347.816 95.0664C348.754 93.6992 349.223 92.4297 349.223 91.2578L353.617 98.875C352.914 100.438 352.055 102.059 351.039 103.738C350.023 105.379 348.734 106.922 347.172 108.367C345.609 109.773 343.715 110.926 341.488 111.824C339.301 112.723 336.664 113.172 333.578 113.172C329.594 113.172 325.98 112.371 322.738 110.77C319.496 109.129 316.898 106.883 314.945 104.031C313.031 101.18 312.074 97.8984 312.074 94.1875C312.074 90.8672 312.68 87.918 313.891 85.3398C315.102 82.7617 316.918 80.5742 319.34 78.7773C321.801 76.9805 324.887 75.6328 328.598 74.7344C332.309 73.7969 336.645 73.3281 341.605 73.3281H350.746ZM397.211 60.7891V136.375H378.93V48.6016H395.98L397.211 60.7891ZM436.762 79.5977V80.8281C436.762 85.4375 436.234 89.7148 435.18 93.6602C434.125 97.5664 432.543 100.984 430.434 103.914C428.363 106.844 425.805 109.129 422.758 110.77C419.711 112.371 416.176 113.172 412.152 113.172C408.324 113.172 405.004 112.371 402.191 110.77C399.418 109.129 397.074 106.863 395.16 103.973C393.285 101.043 391.762 97.7031 390.59 93.9531C389.457 90.1641 388.578 86.1211 387.953 81.8242V79.4219C388.578 74.8516 389.477 70.6133 390.648 66.707C391.82 62.8008 393.344 59.4219 395.219 56.5703C397.094 53.6797 399.418 51.4336 402.191 49.832C404.965 48.2305 408.266 47.4297 412.094 47.4297C416.078 47.4297 419.613 48.1914 422.699 49.7148C425.785 51.2383 428.363 53.4258 430.434 56.2773C432.543 59.0898 434.125 62.4688 435.18 66.4141C436.234 70.3594 436.762 74.7539 436.762 79.5977ZM418.422 80.8281V79.5977C418.422 77.0195 418.227 74.6562 417.836 72.5078C417.445 70.3203 416.82 68.4258 415.961 66.8242C415.102 65.1836 413.969 63.9141 412.562 63.0156C411.156 62.1172 409.438 61.668 407.406 61.668C405.219 61.668 403.363 62.0195 401.84 62.7227C400.316 63.4258 399.086 64.4609 398.148 65.8281C397.211 67.1562 396.527 68.7969 396.098 70.75C395.707 72.7031 395.492 74.9297 395.453 77.4297V83.875C395.492 86.8047 395.902 89.4219 396.684 91.7266C397.504 93.9922 398.773 95.7695 400.492 97.0586C402.25 98.3086 404.594 98.9336 407.523 98.9336C409.594 98.9336 411.312 98.4844 412.68 97.5859C414.086 96.6484 415.199 95.3398 416.02 93.6602C416.879 91.9805 417.484 90.0469 417.836 87.8594C418.227 85.6719 418.422 83.3281 418.422 80.8281ZM464.828 60.7891V136.375H446.547V48.6016H463.598L464.828 60.7891ZM504.379 79.5977V80.8281C504.379 85.4375 503.852 89.7148 502.797 93.6602C501.742 97.5664 500.16 100.984 498.051 103.914C495.98 106.844 493.422 109.129 490.375 110.77C487.328 112.371 483.793 113.172 479.77 113.172C475.941 113.172 472.621 112.371 469.809 110.77C467.035 109.129 464.691 106.863 462.777 103.973C460.902 101.043 459.379 97.7031 458.207 93.9531C457.074 90.1641 456.195 86.1211 455.57 81.8242V79.4219C456.195 74.8516 457.094 70.6133 458.266 66.707C459.438 62.8008 460.961 59.4219 462.836 56.5703C464.711 53.6797 467.035 51.4336 469.809 49.832C472.582 48.2305 475.883 47.4297 479.711 47.4297C483.695 47.4297 487.23 48.1914 490.316 49.7148C493.402 51.2383 495.98 53.4258 498.051 56.2773C500.16 59.0898 501.742 62.4688 502.797 66.4141C503.852 70.3594 504.379 74.7539 504.379 79.5977ZM486.039 80.8281V79.5977C486.039 77.0195 485.844 74.6562 485.453 72.5078C485.062 70.3203 484.438 68.4258 483.578 66.8242C482.719 65.1836 481.586 63.9141 480.18 63.0156C478.773 62.1172 477.055 61.668 475.023 61.668C472.836 61.668 470.98 62.0195 469.457 62.7227C467.934 63.4258 466.703 64.4609 465.766 65.8281C464.828 67.1562 464.145 68.7969 463.715 70.75C463.324 72.7031 463.109 74.9297 463.07 77.4297V83.875C463.109 86.8047 463.52 89.4219 464.301 91.7266C465.121 93.9922 466.391 95.7695 468.109 97.0586C469.867 98.3086 472.211 98.9336 475.141 98.9336C477.211 98.9336 478.93 98.4844 480.297 97.5859C481.703 96.6484 482.816 95.3398 483.637 93.6602C484.496 91.9805 485.102 90.0469 485.453 87.8594C485.844 85.6719 486.039 83.3281 486.039 80.8281Z"
          />
      <circle cx="523" cy="101" r="11" fill="#FD2F78"/>
  </svg>
)

const config: DocsThemeConfig = {
    project: {
        link: 'https://github.com/django-superapp/django-superapp'
    },
    docsRepositoryBase: 'https://github.com/django-superapp/django-superapp/tree/main/docs',
    useNextSeoProps() {
        const {asPath} = useRouter()
        if (asPath !== '/') {
            return {
                titleTemplate: '%s – SuperApp Docs'
            }
        }
    },
    logo,
    head: function useHead() {
        const {title} = useConfig()
        const {route} = useRouter()
        const socialCard =
            route === '/' || !title
                ? 'https://django-superapp.bringes.io/og.jpeg'
                : `https://django-superapp.bringes.io/api/og?title=${title}`

        return (
            <>
                <meta name="msapplication-TileColor" content="#fff"/>
                <meta name="theme-color" content="#fff"/>
                <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                <meta httpEquiv="Content-Language" content="en"/>
                <meta
                    name="description"
                    content="Build your app faster with Django SuperApp."
                />
                <meta
                    name="og:description"
                    content="Build your app faster with Django SuperApp."
                />
                <meta name="twitter:card" content="summary_large_image"/>
                <meta name="twitter:image" content={socialCard}/>
                <meta name="twitter:site:domain" content="django-superapp.bringes.io"/>
                <meta name="twitter:url" content="https://django-superapp.bringes.io"/>
                <meta
                    name="og:title"
                    content={title ? title + ' – SuperApp' : 'SuperApp'}
                />
                <meta name="og:image" content={socialCard}/>
                <meta name="apple-mobile-web-app-title" content="SuperApp"/>
                <link rel="icon" href="/favicon.svg" type="image/svg+xml"/>
                <link rel="icon" href="/favicon.png" type="image/png"/>
                <link
                    rel="icon"
                    href="/favicon-dark.svg"
                    type="image/svg+xml"
                    media="(prefers-color-scheme: dark)"
                />
                <link
                    rel="icon"
                    href="/favicon-dark.png"
                    type="image/png"
                    media="(prefers-color-scheme: dark)"
                />
            </>
        )
    },
    editLink: {
        text: 'Edit this page on GitHub →'
    },
    feedback: {
        content: 'Question? Give us feedback →',
        labels: 'feedback'
    },
    sidebar: {
        titleComponent({title, type}) {
            if (type === 'separator') {
                return <span className="cursor-default">{title}</span>
            }
            return <>{title}</>
        },
        defaultMenuCollapseLevel: 2,
        toggleButton: true
    },
    footer: {
        text: (
            <div className="flex w-full flex-col items-center sm:items-start">
                <p className="mt-6 text-xs">
                    © {new Date().getFullYear()} Django SuperApp. All rights reserved.
                </p>
            </div>
        )
    },
    toc: {
        backToTop: true
    }
}

export default config
