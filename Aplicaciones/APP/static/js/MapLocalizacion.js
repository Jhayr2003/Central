
                    const mapaInicio = document.getElementById("mapa-inicio");
                    const plazaNorteTienda = document.getElementById("plaza-norte");
                    const mapaPlazaNorte = document.getElementById("mapa-plaza-norte");
                    const MegaPlazaTienda = document.getElementById("mega-plaza");
                    const mapaMegaPlaza = document.getElementById("mapa-mega-plaza");
                    const RealPlazaTienda = document.getElementById("real-plaza");
                    const mapaRealPlaza = document.getElementById("mapa-real-plaza");
                    const MallSATienda = document.getElementById("mall-santaanita");
                    const mapaMallSA = document.getElementById("mapa-mall-santaanita");
                    const plazaSurTienda = document.getElementById("plaza-sur");
                    const mapaPlazaSur = document.getElementById("mapa-plaza-sur");
                    const jockeyplazaTienda = document.getElementById("jockey-plaza");
                    const mapaJockeyPlaza = document.getElementById("mapa-jockey-plaza");
                    plazaNorteTienda.addEventListener("click", () => {
                        // Muestra el mapa de Plaza Norte.
                        mapaInicio.style.display = "none";
                        mapaPlazaNorte.style.display = "block";
                        mapaMegaPlaza.style.display = "none";
                        mapaRealPlaza.style.display = "none";
                        mapaMallSA.style.display = "none";
                        mapaPlazaSur.style.display = "none";
                        mapaJockeyPlaza.style.display = "none";
                    });
                    MegaPlazaTienda.addEventListener("click", () => {
                        // Muestra el mapa de Mega Plaza.
                        mapaInicio.style.display = "none";
                        mapaPlazaNorte.style.display = "none";
                        mapaMegaPlaza.style.display = "block";
                        mapaRealPlaza.style.display = "none";
                        mapaMallSA.style.display = "none";
                        mapaPlazaSur.style.display = "none";
                        mapaJockeyPlaza.style.display = "none";
                    });
                    RealPlazaTienda.addEventListener("click", () => {
                        // Muestra el mapa de RealPlaza
                        mapaInicio.style.display = "none";
                        mapaPlazaNorte.style.display = "none";
                        mapaMegaPlaza.style.display = "none";
                        mapaRealPlaza.style.display = "block";
                        mapaMallSA.style.display = "none";
                        mapaPlazaSur.style.display = "none";
                        mapaJockeyPlaza.style.display = "none";
                    });
                    MallSATienda.addEventListener("click", () => {
                        // Muestra el mapa de MallSA
                        mapaInicio.style.display = "none";
                        mapaPlazaNorte.style.display = "none";
                        mapaMegaPlaza.style.display = "none";
                        mapaRealPlaza.style.display = "none";
                        mapaMallSA.style.display = "block";
                        mapaPlazaSur.style.display = "none";
                        mapaJockeyPlaza.style.display = "none";
                    });
                    plazaSurTienda.addEventListener("click", () => {
                        // Muestra el mapa de plaza Sur
                        mapaInicio.style.display = "none";
                        mapaPlazaNorte.style.display = "none";
                        mapaMegaPlaza.style.display = "none";
                        mapaRealPlaza.style.display = "none";
                        mapaMallSA.style.display = "none";
                        mapaPlazaSur.style.display = "block";
                        mapaJockeyPlaza.style.display = "none";
                    });
                    jockeyplazaTienda.addEventListener("click", () => {
                        // Muestra el mapa de JockeyPlaza
                        mapaInicio.style.display = "none";
                        mapaPlazaNorte.style.display = "none";
                        mapaMegaPlaza.style.display = "none";
                        mapaRealPlaza.style.display = "none";
                        mapaMallSA.style.display = "none";
                        mapaPlazaSur.style.display = "none";
                        mapaJockeyPlaza.style.display = "block";
                    });
                    