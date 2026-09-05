export type Opaque<Value, Brand extends string> = Value & {
  readonly __mudacOpaqueBrand: Brand;
};
