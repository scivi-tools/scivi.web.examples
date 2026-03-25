#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from server.app import *


@app.route("/")
@app.route("/index.html")
@app.route("/csv")
def csv_page():
    return LoadEditorPage("kb/csv"), 200, { "Content-Type": "text/html; charset=utf-8" }

@app.route("/es")
def es_page():
    return LoadEditorPage("kb/es"), 200, { "Content-Type": "text/html; charset=utf-8" }

@app.route("/eon")
def eon_page():
    return LoadEditorPage("kb/eon"), 200, { "Content-Type": "text/html; charset=utf-8" }

@app.route("/pong")
def pong_page():
    return LoadEditorPage("kb/pong"), 200, { "Content-Type": "text/html; charset=utf-8" }

@app.route("/shielder")
def shielder_page():
    return LoadEditorPage("kb/shielder"), 200, { "Content-Type": "text/html; charset=utf-8" }

@app.route("/glove")
def glove_page():
    return LoadEditorPage("kb/glove"), 200, { "Content-Type": "text/html; charset=utf-8" }

@app.route("/soc")
def soc_page():
    return LoadEditorPage("kb/soc"),200, { "Content-Type": "text/html; charset=utf-8" }

@app.route("/eeg")
def mxd_page():
    return LoadEditorPage("kb/eeg"), 200, { "Content-Type": "text/html; charset=utf-8" }

@app.route("/bci")
def bci_page():
    return LoadEditorPage("kb/bci"), 200, { "Content-Type": "text/html; charset=utf-8" }

@app.route("/mmaps")
def mmaps_page():
    return LoadEditorPage("kb/mmaps"), 200, { "Content-Type": "text/html; charset=utf-8" }

@app.route("/eye")
def eye_page():
    return LoadEditorPage("kb/eye"), 200, { "Content-Type": "text/html; charset=utf-8" }

@app.route("/locw")
def locw_page():
    return LoadEditorPage("kb/locw"), 200, { "Content-Type": "text/html; charset=utf-8" }

@app.route("/paleo")
def paleo_page():
    return LoadEditorPage("kb/paleo"), 200, { "Content-Type": "text/html; charset=utf-8" }

@app.route("/ttype")
def ttype_page():
    return LoadEditorPage("kb/ttype"), 200, { "Content-Type": "text/html; charset=utf-8" }


@app.route("/exec/<nodeID>")
def srv_exec(nodeID):
    # nodeID = request.args.get("nodeID")
    # instanceID = request.args.get("instanceID")
    # print(str(nodeID) + " " + str(instanceID))
    print(nodeID)
    return "OK"

@app.route("/gen_eon", methods = ["POST"])
def gen_eon():
    dfd = request.get_json(force = True)
    res = None
    try:
        res = getServerInst().gen_eon(dfd)
    except ValueError as err:
        res = { "error": str(err) }
    resp = jsonify(res)
    resp.status_code = 200
    return resp

@app.route("/fwgen/<domain>/<elementName>")
def fwgen(domain, elementName):
    srv = poolServerInst(request.remote_addr, "kb/" + domain)
    f = srv.gen_firmware(elementName)
    if f:
        return f["content"], 200, {'Content-Type': f["mime"], "Content-Disposition": "attachment; filename=\"%s.zip\"" % elementName}
    else:
        return "Not found", 404

@app.route("/scan_ssdp")
def scan_ssdp():
    try:
        res = getServerInst().scan_ssdp()
    except Exception as e:
        print(traceback.format_exc())
        res = None
    if res is not None:
        resp = jsonify(res)
        resp.status_code = 200
        return resp
    else:
        return "Not found", 404
