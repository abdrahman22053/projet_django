// color-modes.js

// Fonction pour activer le mode sombre
function enableDarkMode() {
    document.body.classList.add('dark-mode'); // Ajouter la classe pour le mode sombre
    document.body.classList.remove('light-mode'); // Supprimer la classe pour le mode clair
}

// Fonction pour activer le mode clair
function enableLightMode() {
    document.body.classList.add('light-mode'); // Ajouter la classe pour le mode clair
    document.body.classList.remove('dark-mode'); // Supprimer la classe pour le mode sombre
}

// Écouteurs d'événements pour basculer entre les modes
document.addEventListener('DOMContentLoaded', function () {
    // Écouteur pour le bouton de mode sombre
    const darkModeButton = document.getElementById('dark-mode');
    darkModeButton.addEventListener('click', enableDarkMode);

    // Écouteur pour le bouton de mode clair
    const lightModeButton = document.getElementById('light-mode');
    lightModeButton.addEventListener('click', enableLightMode);
});
