const normalizeSrc = src => {
    return src.startsWith('/') ? src.slice(1) : src;
};

export default function cloudflareLoader ({ src, width, quality }) {
    return `/${normalizeSrc(src)}`;
};