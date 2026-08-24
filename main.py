 #-*- coding: utf-8 -*-
from config import *
from funzioni import *

azienda_sostenibile_dims = dimensione_azienda("sostenibile")
nr_mucche_latte_s = azienda_sostenibile_dims["nr_mucche_latte"]
nr_mucche_carne_s = azienda_sostenibile_dims["nr_mucche_carne"]
nr_ettari_s = azienda_sostenibile_dims["ettari"]
capacita_raccolta_s = azienda_sostenibile_dims["capacita_raccolta"]
monte_ore_gg_s = azienda_sostenibile_dims["monte_ore_gg"]

azienda_intensiva_dims = dimensione_azienda("intensiva")
nr_mucche_latte_i = azienda_intensiva_dims["nr_mucche_latte"]
nr_mucche_carne_i = azienda_intensiva_dims["nr_mucche_carne"]
nr_ettari_i = azienda_intensiva_dims["ettari"]
capacita_raccolta_i = azienda_intensiva_dims["capacita_raccolta"]
monte_ore_gg_i = azienda_intensiva_dims["monte_ore_gg"]


# ---- AZIENDA SOSTENIBILE ----
# 1) calcolo il fabbisogno di ore  2) lo ripartisco per priorità
ore_s = fabbisogno_ore_giornaliero(nr_mucche_latte_s, nr_mucche_carne_s, nr_ettari_s)
rip_s = ripartizione_ore_priorita(monte_ore_gg_s,
                                  ore_s["ore_latte"], ore_s["ore_carne"], ore_s["ore_fieno"])

report_sostenibile = {
    "tipo"           : "Sostenibile",
    "nr_mucche_latte": nr_mucche_latte_s,
    "nr_mucche_carne": nr_mucche_carne_s,
    "nr_ettari"      : nr_ettari_s,
    "monte_ore_gg"   : monte_ore_gg_s,
    "ore"            : ore_s,
    "ripartizione"   : rip_s,
    # le produzioni sono scalate dalla copertura oraria di ciascuna attività
    "litri_latte"    : produzione_latte(
                           nr_mucche_latte_s,
                           params_azienda_sostenibile["resa_giornaliera_latte_per_mucca"],
                           gg_simulazione,
                           fattore_lavoro=rip_s["copertura_latte"]),
    "kg_carne"       : produzione_carne(
                           nr_mucche_carne_s,
                           params_azienda_sostenibile["gg_ingrasso"],
                           gg_simulazione,
                           fattore_lavoro=rip_s["copertura_carne"]),
    "kg_fieno"       : produzione_fieno(
                           nr_ettari_s,
                           params_azienda_sostenibile["resa_ettaro_anno_fieno_kg"],
                           gg_simulazione,
                           fattore_lavoro=rip_s["copertura_fieno"]),
    "costo_totale"   : costo_azienda(
                           nr_mucche_latte_s + nr_mucche_carne_s,
                           nr_ettari_s,
                           params_azienda_sostenibile,
                           gg_simulazione),
}

fabbisogno_s, surplus_s = calcolo_autosufficienza_mangime(
    report_sostenibile["kg_fieno"],
    nr_mucche_latte_s, fieno_mucca_latte_kg_giornaliero,
    nr_mucche_carne_s, fieno_mucca_carne_kg_giornaliero,
    gg_simulazione
)
report_sostenibile["fabbisogno_fieno"] = fabbisogno_s
report_sostenibile["surplus_deficit"]  = surplus_s
report_sostenibile["tempi"] = tempo_produzione(
    nr_mucche_latte_s,
    params_azienda_sostenibile["resa_giornaliera_latte_per_mucca"],
    params_azienda_sostenibile["gg_ingrasso"],
    nr_ettari_s,
    params_azienda_sostenibile["resa_ettaro_anno_fieno_kg"],
    capacita_raccolta_s
)


# ---- AZIENDA INTENSIVA ----
ore_i = fabbisogno_ore_giornaliero(nr_mucche_latte_i, nr_mucche_carne_i, nr_ettari_i)
rip_i = ripartizione_ore_priorita(monte_ore_gg_i,
                                  ore_i["ore_latte"], ore_i["ore_carne"], ore_i["ore_fieno"])

report_intensiva = {
    "tipo"           : "Intensiva",
    "nr_mucche_latte": nr_mucche_latte_i,
    "nr_mucche_carne": nr_mucche_carne_i,
    "nr_ettari"      : nr_ettari_i,
    "monte_ore_gg"   : monte_ore_gg_i,
    "ore"            : ore_i,
    "ripartizione"   : rip_i,
    "litri_latte"    : produzione_latte(
                           nr_mucche_latte_i,
                           params_azienda_intensiva["resa_giornaliera_latte_per_mucca"],
                           gg_simulazione,
                           fattore_lavoro=rip_i["copertura_latte"]),
    "kg_carne"       : produzione_carne(
                           nr_mucche_carne_i,
                           params_azienda_intensiva["gg_ingrasso"],
                           gg_simulazione,
                           fattore_lavoro=rip_i["copertura_carne"]),
    "kg_fieno"       : produzione_fieno(
                           nr_ettari_i,
                           params_azienda_intensiva["resa_ettaro_anno_fieno_kg"],
                           gg_simulazione,
                           fattore_lavoro=rip_i["copertura_fieno"]),
    "costo_totale"   : costo_azienda(
                           nr_mucche_latte_i + nr_mucche_carne_i,
                           nr_ettari_i,
                           params_azienda_intensiva,
                           gg_simulazione),
}

fabbisogno_i, surplus_i = calcolo_autosufficienza_mangime(
    report_intensiva["kg_fieno"],
    nr_mucche_latte_i, fieno_mucca_latte_kg_giornaliero,
    nr_mucche_carne_i, fieno_mucca_carne_kg_giornaliero,
    gg_simulazione
)
report_intensiva["fabbisogno_fieno"] = fabbisogno_i
report_intensiva["surplus_deficit"]  = surplus_i
report_intensiva["tempi"] = tempo_produzione(
    nr_mucche_latte_i,
    params_azienda_intensiva["resa_giornaliera_latte_per_mucca"],
    params_azienda_intensiva["gg_ingrasso"],
    nr_ettari_i,
    params_azienda_intensiva["resa_ettaro_anno_fieno_kg"],
    capacita_raccolta_i
)


confronto(report_sostenibile, report_intensiva)
genera_grafici_confronto(report_sostenibile, report_intensiva)
genera_grafico_ripartizione_ore(report_sostenibile, report_intensiva)
salva_report_pdf(report_sostenibile, report_intensiva)
