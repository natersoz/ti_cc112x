/**
 * @file ti_cc_iocfg.h
 *
 * @copyright Copyright (c) 2024 natersoz under the Apache 2.0 license.
 */

#pragma once

#include <cstddef>
#include <cstdint>

#include "bit_manip.h"

#if 0
namespace ti_cc
{

template<typename ... Fields>
class reg
{
    char const* const name;
    uint8_t const     address;

    struct field
    {
        char const* const name;
        uint8_t const     pos;
        uint8_t const     bits;
    };

    using field_count = sizeof...(Fields);

    std::array<field, field_count> const fields;

};

}; // namespace ti_cc

ti_cc::reg iocfg_3 = {
    .name    = "IOCFG3",
    .address = 0x00,
};

#endif

namespace ti_cc
{
namespace regs
{

enum gpio_config {
    RXFIFO_THR      = 0,
    RXFIFO_THR_PKT  = 1,
};


struct iocfg_3
{
    using value_type   = uint8_t;
    using address_type = uint8_t;

    static constexpr value_type   reset_value = 0x00u;
    static constexpr address_type address     = 0x00u;

    value_type value;

    struct atran
    {
        using value_type                   = bool;
        static constexpr uint8_t bit_pos   = 7u;
        static constexpr uint8_t bit_width = 1u;
    };
    struct invert
    {
        using value_type                   = bool;
        static constexpr uint8_t bit_pos   = 6u;
        static constexpr uint8_t bit_width = 1u;
    };
    struct config
    {
        using value_type                   = gpio_config;
        static constexpr uint8_t bit_pos   = 0u;
        static constexpr uint8_t bit_width = 6u;
    };

    iocfg_3() : value(reset_value) {}

    template<typename FieldType>
    constexpr typename FieldType::value_type get() const
    {
        // The return type FieldType::value_type might be an enum, bool, etc.
        // so cast to the return type from the integer type value_type.
        return
            static_cast<typename FieldType::value_type>(
                bit_manip::value_get(this->value,
                                     FieldType::bit_width,
                                     FieldType::bit_pos));

    }

    template<typename FieldType>
    constexpr void set(typename FieldType::value_type field_value)
    {
        // field_value might be an enum, bool, etc. so cast: to value_type.
        this->value = bit_manip::value_set(this->value,
                                           static_cast<value_type>(field_value),
                                           FieldType::bit_width,
                                           FieldType::bit_pos);
    }

    constexpr void reset() { this->value = reset_value; }
};

}; // namespace regs
}; // namespace ti_cc
