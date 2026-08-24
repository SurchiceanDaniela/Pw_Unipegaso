# -*- coding: utf-8 -*-

costo_acqua         = 0.20
costo_fertilizzante = 0.80
fieno_mucca_latte_kg_giornaliero = 17
fieno_mucca_carne_kg_giornaliero = 13
gg_simulazione = 365
raccolta_fieno_ettari_giornaliero = 1
gestione_mucca_latte = 0.3
gestione_mucca_carne = 0.5

params_azienda_sostenibile = {
    "resa_giornaliera_latte_per_mucca"     : 15,
    "gg_ingrasso"                          : 600,
    "resa_ettaro_anno_fieno_kg"            : 4000,
    "acqua_animali_giornaliera_media_litri": 100,
    "acqua_irrigazione_ettaro_m3_anno"     : 6000,
    "fertilizzanti_ettaro_kg_anno"         : 0
    }

params_azienda_intensiva = {
    "resa_giornaliera_latte_per_mucca"     : 25,
    "gg_ingrasso"                          : 420,
    "resa_ettaro_anno_fieno_kg"            : 6000,
    "acqua_animali_giornaliera_media_litri": 150,
    "acqua_irrigazione_ettaro_m3_anno"     : 7000,
    "fertilizzanti_ettaro_kg_anno"         : 1000}
