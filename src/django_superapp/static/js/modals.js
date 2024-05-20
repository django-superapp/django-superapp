const dismissModal = (modalName) => {
    console.debug("Dismissing modal", modalName)
    document.querySelector(`div.window-modal-wrapper[id="window-modal-wrapper-${modalName}"]`)?.remove();
    document.querySelector(`div.window-modal-backdrop[id="window-modal-backdrop-${modalName}"]`)?.remove();
}

// Patch the dismiss functions to remove the iframe when the modal is closed
const originalDismissChangeRelatedObjectPopup = dismissChangeRelatedObjectPopup;
const originalDismissDeleteRelatedObjectPopup = dismissDeleteRelatedObjectPopup;
const originalDismissAddRelatedObjectPopup = dismissAddRelatedObjectPopup;

// Reassigning modified functions
dismissChangeRelatedObjectPopup = (...args) => {
    originalDismissChangeRelatedObjectPopup(...args);
    dismissModal(args[0]?.name);
};

dismissDeleteRelatedObjectPopup = (...args) => {
    originalDismissDeleteRelatedObjectPopup(...args);
    dismissModal(args[0]?.name);
};

dismissAddRelatedObjectPopup = (...args) => {
    originalDismissAddRelatedObjectPopup(...args);
    dismissModal(args[0]?.name);
};

// Patch window.open to open an iframe instead of a new window
const originalWindowOpen = window.open;
window.open = function (url, name, features) {
    console.debug("Opening window in modal", url, name, features)
    const openedWindowsIdx = parseInt(name.split("__")[-1] ?? "0");
    // Create backdrop element
    const backdrop = document.createElement("div");
    backdrop.className = "window-modal-backdrop";
    backdrop.style.cssText = `
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;    
    z-index: ${50 + openedWindowsIdx};
    background-color: #111827ab;
  `;
    backdrop.id = `window-modal-backdrop-${name}`
    backdrop.setAttribute("name", name);
    backdrop.addEventListener("click", function (e) {
        e.stopPropagation();
        dismissModal(this.getAttribute('name'));
    });
    document.body.appendChild(backdrop);

    const iframeModalWrapper = document.createElement("div");
    iframeModalWrapper.id = `window-modal-wrapper-${name}`;
    iframeModalWrapper.className = "window-modal-wrapper";
    iframeModalWrapper.setAttribute("name", name);
    iframeModalWrapper.style.cssText = `
    z-index: ${50 + openedWindowsIdx};
    background: white;
    border: 3px solid #e2e2e2;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 800px;
    height: 500px;
  `;

    // Create iframe element
    const iframeModal = document.createElement("iframe");
    iframeModal.id = `window-modal-${name}`;
    // iframeModal.name = name;
    iframeModal.setAttribute("name", name);
    iframeModal.className = "window-modal";
    iframeModal.src = url; // Set iframe src
    iframeModal.style.cssText = `
    width: 100%;
    height: 100%;
  `;

    const closeButton = document.createElement("div");
    closeButton.className = "window-modal-close";
    closeButton.innerHTML = "X";
    closeButton.style.cssText = `
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(calc(-50% + 383px), calc(-50% - 231px));
    color: white;
    z-index: ${51 + openedWindowsIdx};
    cursor: pointer;
    background: #aeaeae;
    padding: 5px 10px;
  `;
    closeButton.addEventListener("click", function (e) {
        e.stopPropagation();
        dismissModal(this.parentElement.getAttribute('name'));
    });

    iframeModalWrapper.appendChild(closeButton);
    iframeModalWrapper.appendChild(iframeModal);

    document.body.appendChild(iframeModalWrapper);

    const w = originalWindowOpen(url, name, features);
    console.log(w);
    return w;

}