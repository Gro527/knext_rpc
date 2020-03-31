namespace py knowledge_extraction

struct ExtReq {
    1: required string text;
    255: required string caller
}

struct Knowledge {
    1: required string subject;
    2: required string relation;
    3: required string object
}

struct ExtRsp {
    1: required string text;
    2: required list<Knowledge> kn;
    255: required string server_info;
}

struct BadCaseReq {
    1: required list<Knowledge> badcases;
    255: required string caller
}

struct BadCaseRsp {
    1: required binary retcode;
    255: required string server_info;
}

service ExtractionService {
    ExtRsp get_extraction(1:ExtReq req)
    BadCaseRsp set_badcase(1:BadCaseReq req)
}
