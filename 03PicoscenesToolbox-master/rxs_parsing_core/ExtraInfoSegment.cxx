//
// Created by Zhiping Jiang on 2020/11/6.
//

#include "ExtraInfoSegment.hxx"

static auto parserWrapper = [](const uint8_t *buffer, uint32_t bufferLength) -> ExtraInfo {
    if (auto eiOpt = ExtraInfo::fromBuffer(buffer, 0)) {
        auto calculatedLength = eiOpt->calculateBufferLength();
        if (calculatedLength != bufferLength - 4)
            throw std::runtime_error("ExtraInfoSegment cannot decode due to the mismatched buffer length.");
        return eiOpt.value();
    }

    throw std::runtime_error("ExtraInfoSegment cannot decode the given buffer.");
};

std::map<uint16_t, std::function<ExtraInfo(const uint8_t *, uint32_t)>> ExtraInfoSegment::versionedSolutionMap = initializeSolutionMap();

std::map<uint16_t, std::function<ExtraInfo(const uint8_t *, uint32_t)>> ExtraInfoSegment::initializeSolutionMap() noexcept {
    return std::map<uint16_t, std::function<ExtraInfo(const uint8_t *, uint32_t)>>{{0x1U, parserWrapper},
                                                                                   {0x2U, parserWrapper}};
}

ExtraInfoSegment::ExtraInfoSegment() : AbstractPicoScenesFrameSegment("ExtraInfo", 0x2U) {}

ExtraInfoSegment::ExtraInfoSegment(const ExtraInfo &extraInfoV) : ExtraInfoSegment() {
    extraInfo = extraInfoV;
    setSegmentPayload(extraInfoV.toBuffer());
}

ExtraInfoSegment::ExtraInfoSegment(const uint8_t *buffer, uint32_t bufferLength) : AbstractPicoScenesFrameSegment(buffer, bufferLength) {
    if (segmentName != "ExtraInfo")
        throw std::runtime_error("ExtraInfoSegment cannot parse the segment named " + segmentName + ".");
    if (!versionedSolutionMap.count(segmentVersionId))
        throw std::runtime_error("ExtraInfoSegment cannot parse the segment with version v" + std::to_string(segmentVersionId) + ".");

    extraInfo = versionedSolutionMap.at(segmentVersionId)(segmentPayload.data(), segmentPayload.size());
}

const ExtraInfo &ExtraInfoSegment::getExtraInfo() const {
    return extraInfo;
}

void ExtraInfoSegment::setExtraInfo(const ExtraInfo &extraInfo) {
    ExtraInfoSegment::extraInfo = extraInfo;
    setSegmentPayload(extraInfo.toBuffer());
}
